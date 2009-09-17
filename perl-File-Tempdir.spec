#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Tempdir
Summary:	File::Tempdir - interface to tempdir()
Summary(pl.UTF-8):	File::Tempdir - interfejs do tempdir()
Name:		perl-File-Tempdir
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/N/NA/NANARDON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	51f609343908803bbc78774ceb81c431
URL:		http://search.cpan.org/dist/File-Tempdir/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provide an object interface to tempdir() from File::Temp.
This allow to destroy the temporary directory as soon you don't need
it anymore using the magic DESTROY() function automatically call be
perl when the object is no longer reference.

If a value is passed to at object creation, it become only a container
allowing to keep same code in your function.

%description -l pl.UTF-8
Moduł ten dostarcza interfejs do tempdir() dla File::Temp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/File/*.pm
%{_mandir}/man3/*
