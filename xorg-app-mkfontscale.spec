Summary:	mkfontscale application
Summary(pl.UTF-8):   Aplikacja mkfontscale
Name:		xorg-app-mkfontscale
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/mkfontscale-%{version}.tar.bz2
# Source0-md5:	1d608771aca9695b828cec1e34178fd1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mkfontscale application.

%description -l pl.UTF-8
Aplikacja mkfontscale.

%prep
%setup -q -n mkfontscale-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1x*
