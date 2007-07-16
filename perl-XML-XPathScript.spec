%define module  XML-XPathScript
%define name    perl-%{module}
%define version 1.52
%define release %mkrel 1

%define _requires_exceptions perl(Apache)\\|perl(Apache::AxKit::Cache)\\|perl(Apache::AxKit::CharsetConv)\\|perl(Apache::AxKit::Exception)\\|perl(Apache::AxKit::Language)\\|perl(Apache::AxKit::Provider)\\|perl(Apache::File)

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A Perl framework for XML stylesheets
License:        Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(XML::XPath)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Clone)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}


%description
%{module} is an XML templating language that has some concepts from ASP
and some from XSLT. This makes for a very flexible option for transforming
XML to HTML or text or just about any other format.

%prep
%setup -q -n %{module}-%{version}

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
