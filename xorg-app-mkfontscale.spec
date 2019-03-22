Summary:	mkfontscale and mkfontdir applications - create an index of font files for X
Summary(pl.UTF-8):	Aplikacje mkfontscale i mkfontdir - tworzenie indeksu plików fontów dla X
Name:		xorg-app-mkfontscale
Version:	1.2.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/mkfontscale-%{version}.tar.bz2
# Source0-md5:	215940de158b1a3d8b3f8b442c606e2f
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.25
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	zlib-devel
Provides:	xorg-app-mkfontdir = %{version}-%{release}
Obsoletes:	xorg-app-mkfontdir < 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by
the legacy X11 font system.

mkfontdir creates the fonts.dir files needed by the legacy X server
core font system. The current implementation is a simple wrapper
script around the mkfontscale program, which must be installed first.

%description -l pl.UTF-8
mkfontscale tworzy pliki indeksów fonts.scale i fonts.dir używane
przez stary system fontów X11.

mkfontdir tworzy pliki fonts.dir wymagane przez stary system fontów
serwera X. Aktualna implementacja to prosty skrypt obudowujący program
mkfontscale, który musi być wcześniej zainstalowany.

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/mkfontdir
%attr(755,root,root) %{_bindir}/mkfontscale
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*
