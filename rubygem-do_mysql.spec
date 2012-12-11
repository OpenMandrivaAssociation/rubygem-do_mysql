# Generated from do_mysql-0.10.7.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	do_mysql

Summary:	DataObjects MySQL Driver
Name:		rubygem-%{rbname}
Url:		http://rubygems.org/gems/do_mysql
Version:	0.10.7
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	mysql-devel

%description
Implements the DataObjects API for MySQL

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/do_mysql
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/do_mysql/*.rb
%{ruby_sitearchdir}/%{rbname}/do_mysql.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.markdown
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.7-3
+ Revision: 774501
- drop dependency on rake, it's now provided by ruby's standard library
- mass rebuild of ruby packages against ruby 1.9.1

* Tue Jan 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.10.7-1
+ Revision: 767881
- BR:mysql-devel
- imported package rubygem-do_mysql

