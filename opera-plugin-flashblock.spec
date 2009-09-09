# TODO:
# - License
# - doesn't work the "styles" directory - what's the correct place?
Summary:	Replaces Flash objects with a button you can click to view them
Summary(hu.UTF-8):	Flash objektumokat cseréli ki egy gombra, amelyre kattintva megnézheted
Name:		opera-plugin-flashblock
Version:	1.6.9
Release:	0.1
License:	unknown
Group:		Applications
Source0:	http://ruzanow.ru/opera/flashblocker.zip
# Source0-md5:	dddb58f7468860adc4c4ac72425a0ecc
URL:		http://my.opera.com/Lex1/blog/flashblock-for-opera-9
Requires:	opera >= 10.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define operadir %{_datadir}/opera
%define operastyles %{operadir}/styles/user
%define operascripts %{operadir}/scripts

%description
Replaces Flash objects with a button you can click to view them.

%description -l hu.UTF-8
Flash objektumokat cseréli ki egy gombra, amelyre kattintva
megnézheted.

%prep
%setup -q -c -n flashblock

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{operastyles}
install -d $RPM_BUILD_ROOT%{operascripts}

install FlashBlocker.css $RPM_BUILD_ROOT%{operastyles}
install FlashBlocker.js $RPM_BUILD_ROOT%{operascripts}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FlashBlocker-info*
%{operastyles}/*
%{operascripts}/*
