# TODO:
# - License
Summary:	Replaces Flash objects with a button you can click to view them
Summary(hu.UTF-8):	Flash objektumokat cseréli ki egy gombra, amelyre kattintva megnézheted
Name:		opera-plugin-flashblock
Version:	1.6.9
Release:	1
License:	unknown
Group:		X11/Applications/Networking
Source0:	http://ruzanow.ru/opera/flashblocker.zip
# Source0-md5:	dddb58f7468860adc4c4ac72425a0ecc
Source1:	install-%{name}
URL:		http://my.opera.com/Lex1/blog/flashblock-for-opera-9
Requires:	opera >= 10.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define operadir %{_datadir}/opera
%define operastyles %{operadir}/styles/user
%define operascripts %{operadir}/scripts

%description
Replaces Flash objects with a button you can click to view them. After
install you should run 'install-%{name}' as user.

%description -l hu.UTF-8
Flash objektumokat cseréli ki egy gombra, amelyre kattintva
megnézheted. Telepítés után felhasználóként le kell futtatnod az
'install-%{name}' szkriptet.

%prep
%setup -q -c -n flashblock

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{operastyles}
install -d $RPM_BUILD_ROOT%{operascripts}
install -d $RPM_BUILD_ROOT%{_bindir}

install FlashBlocker.css $RPM_BUILD_ROOT%{operastyles}
install FlashBlocker.js FlashBlocker-white-list.js $RPM_BUILD_ROOT%{operascripts}
install %SOURCE1 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/install-opera-plugin-flashblock
%doc FlashBlocker-info*
%{operastyles}/*
%{operascripts}/*
