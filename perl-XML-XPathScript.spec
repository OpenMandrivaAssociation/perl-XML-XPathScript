%define upstream_name    XML-XPathScript
%define upstream_version 1.54

%define _requires_exceptions perl(Apache)\\|perl(Apache::AxKit::Cache)\\|perl(Apache::AxKit::CharsetConv)\\|perl(Apache::AxKit::Exception)\\|perl(Apache::AxKit::Language)\\|perl(Apache::AxKit::Provider)\\|perl(Apache::File)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A Perl framework for XML stylesheets
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Clone)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} is an XML templating language that has some concepts from ASP
and some from XSLT. This makes for a very flexible option for transforming
XML to HTML or text or just about any other format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes script
%{_mandir}/*/*
%{perl_vendorlib}/XML
%{_bindir}/xpathscript


%changelog
* Mon Aug 03 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 1.540.0-1mdv2010.0
+ Revision: 408258
- rebuild using %%perl_convert_version

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.54-1mdv2009.0
+ Revision: 270417
- update to new version 1.54

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.53-4mdv2009.0
+ Revision: 258882
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.53-3mdv2009.0
+ Revision: 246785
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.53-1mdv2008.1
+ Revision: 135950
- update to new version 1.53

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.52-1mdv2008.0
+ Revision: 52531
- update to new version 1.52

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.50-1mdv2008.0
+ Revision: 47923
- fix build dependencies
- update to new version 1.50

* Mon Apr 30 2007 Nicolas L√©cureuil <neoclust@mandriva.org> 1.49-1mdv2008.0
+ Revision: 19391
-New version


* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 20:58:30 (59655)
- 1.45

* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 20:50:10 (59654)
Import perl-XML-XPathScript

* Fri Aug 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.44-1mdv2007.0
- new version 
- fix sources URL
- fix license

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.41-1mdv2007.0
- New version 1.41

* Wed May 03 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 1.01-2mdk
- Fix According to perl Policy
    - BuildRequires

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdk
- New release 1.01
- spec cleanup
- fix source URL

* Tue Jan 03 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.16-1mdk
- New release 0.16
- fix source to make rpmbuilupdate friendly

* Thu Sep 29 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.15-2mdk
- Fix BuildRequires

* Mon Jul 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-1mdk
- 0.15

* Wed Nov 10 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.14-2mdk
- Remove requires for AxKit modules

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.14-1mdk
- 0.14

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.11-2mdk
- own dir

* Fri Jan 23 2004 Per ÿyvind Karlsen <peroyvind@linux-mandrake.com> 0.11-1mdk
- 0.11
- add url tag

