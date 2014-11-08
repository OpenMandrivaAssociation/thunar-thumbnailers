%define url_ver %(echo %{version} | cut -c 1-3)
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A thumbnail plugin for the Thunar File Manager
Name:		thunar-thumbnailers
Version:	0.4.1
Release:	8.1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-thumbnailers
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(thunarx-2)
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	unzip
BuildRequires:	dcraw
BuildRequires:	ffmpegthumbnailer
#BuildRequires:	grace
BuildRequires:	texlive-latex
Requires:	thunar >= 0.8.0
Requires:	imagemagick
Requires:	unzip
Suggests:	%{name}-ffmpeg

%description
Thumbnails support for Thunar File Manager.

%package ffmpeg
Summary:	A ffmpeg thumbnails support for Thunar File Manager
Group:		Graphical desktop/Xfce
Requires:	ffmpegthumbnailer
Requires:	%{name}

%description ffmpeg
A ffmpeg thumbnails support for Thunar File Manager.

%package grace
Summary:	A grace thumbnails support for Thunar File Manager
Group:		Graphical desktop/Xfce
Requires:	grace
Requires:	%{name}

%description grace
A grace thumbnails support for Thunar File Manager.

%package raw
Summary:	A RAW thumbnails support for Thunar File Manager
Group:		Graphical desktop/Xfce
Requires:	dcraw
Requires:	%{name}

%description raw
A RAW thumbnails support for Thunar File Manager.

%package tex
Summary:	A TEX thumbnails support for Thunar File Manager
Group:		Graphical desktop/Xfce
Requires:	texlive-latex
Requires:	%{name}

%description tex
A TEX thumbnails support for Thunar File Manager.

%prep
%setup -q

%build
%configure \
	--enable-raw \
	--disable-grace \
	--enable-ffmpeg \
	--enable-tex
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README
%dir %{_datadir}/thumbnailers
%{_libdir}/dvi-thumbnailer
%{_libdir}/eps-thumbnailer
%{_libdir}/fig-thumbnailer
%{_libdir}/odf-thumbnailer
%{_libdir}/pdf-thumbnailer
%{_libdir}/ps-thumbnailer
%{_libdir}/psd-thumbnailer
%{_libdir}/svgz-thumbnailer
%{_libdir}/xcf-thumbnailer
%{_datadir}/mime/packages/thunar-thumbnailers.xml
%{_datadir}/thumbnailers/dvi-thumbnailer.desktop
%{_datadir}/thumbnailers/eps-thumbnailer.desktop
%{_datadir}/thumbnailers/fig-thumbnailer.desktop
%{_datadir}/thumbnailers/odf-thumbnailer.desktop
%{_datadir}/thumbnailers/pdf-thumbnailer.desktop
%{_datadir}/thumbnailers/ps-thumbnailer.desktop
%{_datadir}/thumbnailers/psd-thumbnailer.desktop
%{_datadir}/thumbnailers/svgz-thumbnailer.desktop
%{_datadir}/thumbnailers/xcf-thumbnailer.desktop

%files ffmpeg
%{_libdir}/ffmpeg-thumbnailer
%{_libdir}/ogg-thumbnailer
%{_datadir}/thumbnailers/ffmpeg-thumbnailer.desktop
%{_datadir}/thumbnailers/ogg-thumbnailer.desktop

%files grace
%{_libdir}/agr-thumbnailer
%{_datadir}/thumbnailers/agr-thumbnailer.desktop

%files raw
%{_libdir}/raw-thumbnailer
%{_datadir}/thumbnailers/raw-thumbnailer.desktop

%files tex
%{_libdir}/tex-thumbnailer
%{_datadir}/thumbnailers/tex-thumbnailer.desktop
