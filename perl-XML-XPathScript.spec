%define upstream_name    XML-XPathScript
%define upstream_version 1.54

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

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
./Build install destdir=%{buildroot}

%files
%doc README Changes script
%{_mandir}/*/*
%{perl_vendorlib}/XML
%{_bindir}/xpathscript
