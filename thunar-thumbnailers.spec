%define url_ver			%(echo %{version} | cut -c 1-3)
%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Summary:	A thumbnail plugin for the Thunar File Manager
Name:		thunar-thumbnailers
Version:	0.4.1
Release:	8
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-thumbnailers
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel >= 0.8.0
BuildRequires:	imagemagick
BuildRequires:	perl(XML::Parser)
BuildRequires:	unzip
BuildRequires:	dcraw
BuildRequires:	ffmpegthumbnailer
BuildRequires:	grace
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
%configure2_5x \
	--enable-raw \
	--enable-grace \
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


%changelog
* Fri Apr 29 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-6mdv2011.0
+ Revision: 660730
- rebuild

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-5mdv2011.0
+ Revision: 615214
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-4mdv2010.1
+ Revision: 543284
- rebuild for mdv 2010.1

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-3mdv2009.1
+ Revision: 349184
- rebuild whole xfce

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-2mdv2009.1
+ Revision: 294892
- rebuild for new Thunar  (Xfce4.6 beta1)

* Mon Sep 01 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.1-1mdv2009.0
+ Revision: 278572
- update to new version 0.4.1

* Sun Jul 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-1mdv2009.0
+ Revision: 234212
- update file list
- update to new version 0.4.0
- drop requires on raw-thumbnailer since upstream starts to rely on dcraw
- run scriplets only for mdv older than 2009

* Mon May 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-2mdv2009.0
+ Revision: 206161
- split out the package (#40765)
- correct the requires and buildrequires
- do not generate debug package, since this software is a couple of bash scripts
- fix file list

* Tue Mar 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 188443
- new version

* Mon Mar 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-1mdv2008.1
+ Revision: 178004
- new version
- enable support for tex, dcraw and raw-thumbnailer

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-3mdv2008.1
+ Revision: 110640
- new license policy
- do not package COPYING and INSTALL files

* Sun Sep 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-3mdv2008.0
+ Revision: 83580
- do not use evince to generate pdf thumbnails

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-2mdv2008.0
+ Revision: 71435
- add buildrequires on ffmpegthumbnailer,evince and grace, so the proper funcionality could be enabled
- disable grace support for now
- add proper requires to support generating thumbnails

* Sat Aug 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 65457
- fix file list
- new version
- add requires on imagemagick
- own directory
- new version

* Sat Jun 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 40286
- new version
- s/imagemagick/ImageMagick

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-3mdv2008.0
+ Revision: 30504
- fix typo

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-2mdv2008.0
+ Revision: 30502
- update summary

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1mdv2008.0
+ Revision: 30342
- Import thunar-thumbnailers

