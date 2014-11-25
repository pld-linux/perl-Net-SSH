#
# Conditional build:
%bcond_without	tests # do not perform "make test"

%define		pdir	Net
%define		pnam	SSH
%include	/usr/lib/rpm/macros.perl
Summary:	Net::SSH Perl module
Summary(cs.UTF-8):	Modul Net::SSH pro Perl
Summary(da.UTF-8):	Perlmodul Net::SSH
Summary(de.UTF-8):	Net::SSH Perl Modul
Summary(es.UTF-8):	Módulo de Perl Net::SSH
Summary(fr.UTF-8):	Module Perl Net::SSH
Summary(it.UTF-8):	Modulo di Perl Net::SSH
Summary(ja.UTF-8):	Net::SSH Perl モジュール
Summary(ko.UTF-8):	Net::SSH 펄 모줄
Summary(nb.UTF-8):	Perlmodul Net::SSH
Summary(pl.UTF-8):	Moduł Perla Net::SSH
Summary(pt.UTF-8):	Módulo de Perl Net::SSH
Summary(pt_BR.UTF-8):	Módulo Perl Net::SSH
Summary(ru.UTF-8):	Модуль для Perl Net::SSH
Summary(sv.UTF-8):	Net::SSH Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Net::SSH
Summary(zh_CN.UTF-8):	Net::SSH Perl 模块
Name:		perl-Net-SSH
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	96837a66d0329e49cf5febd8b1ff4315
URL:		http://search.cpan.org/dist/Net-SSH/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SSH - perl wrapper for system 'ssh' command

%description -l pl.UTF-8
Net::SSH - interfejs do systemowego polecenia 'ssh'

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/SSH.pm
%{_mandir}/man3/*
