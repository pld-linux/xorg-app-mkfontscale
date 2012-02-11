Summary:	mkfontscale application - create an index of scalable font files for X
Summary(pl.UTF-8):	Aplikacja mkfontscale - tworzenie indeksu plików fontów skalowalnych dla X
Name:		xorg-app-mkfontscale
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/mkfontscale-%{version}.tar.bz2
# Source0-md5:	414fcb053418fb1418e3a39f4a37e0f7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by
the legacy X11 font system.

%description -l pl.UTF-8
mkfontscale tworzy pliki indeksów fonts.scale i fonts.dir używane
przez stary system fontów X11.

%prep
%setup -q -n mkfontscale-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-bzip2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/mkfontscale
%{_mandir}/man1/mkfontscale.1x*
