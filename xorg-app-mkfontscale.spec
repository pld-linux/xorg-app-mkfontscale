# $Rev: 3356 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	mkfontscale application
Summary(pl):	Aplikacja mkfontscale
Name:		xorg-app-mkfontscale
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/mkfontscale-%{version}.tar.bz2
# Source0-md5:	9a4532c4748a85f3dedcf29c841aad82
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/mkfontscale-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
mkfontscale application.

%description -l pl
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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
