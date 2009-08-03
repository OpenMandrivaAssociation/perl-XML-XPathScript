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
