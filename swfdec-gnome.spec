Summary:	GNOME integration for swfdec Flash rendering library
Summary(pl.UTF-8):	Integracja z GNOME biblioteki renderującej animacje Flash swfdec
Name:		swfdec-gnome
Version:	2.24.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://download.gnome.org/sources/swfdec-gnome/2.24/%{name}-%{version}.tar.gz
# Source0-md5:	a5f0eb64b77663b8e8b98d1909a5d52f
URL:		http://swfdec.freedesktop.org/wiki/
# just gconftool-2
BuildRequires:	GConf2
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.6
BuildRequires:	gnome-common >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	swfdec-devel >= 0.8.0
BuildRequires:	swfdec-gtk-devel >= 0.8.0
# for thumbnailer
Requires(post,preun):	GConf2
Requires(post,postun):	hicolor-icon-theme
Requires:	swfdec-gtk >= 0.8.0
Obsoletes:	swfdec-icons <= 0.7.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains programs to integrate Flash functionality
provided by swfdec libraries into the GNOME desktop. Its main
application is swfdec-player, a stand-alone viewer for Flash files. It
also contains swfdec-thumbnailer, a program that provides screenshots
for files to display in the Nautilus file manager.

%description -l pl.UTF-8
Ten pakiet zawiera programy integrujące obsługę plików Flash
zapewnianą przez biblioteki swfdec ze środowiskiem GNOME. Główna
aplikacja to swfdec-player - samodzielny odtwarzacz plików Flash.
Pakiet zawiera także program swfdec-thumbnailer, dostarczajacy migawki
plików do wyświetlania w zarządcy plików Nautilus.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install swfdec-thumbnailer.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall swfdec-thumbnailer.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
# player
%attr(755,root,root) %{_bindir}/swfdec-player
%{_datadir}/swfdec-gnome
%{_desktopdir}/swfdec-player.desktop
# thumbnailer
%attr(755,root,root) %{_bindir}/swfdec-thumbnailer
%{_sysconfdir}/gconf/schemas/swfdec-thumbnailer.schemas
%{_mandir}/man1/*
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
