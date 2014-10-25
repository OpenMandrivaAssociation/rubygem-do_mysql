
%define	rbname	do_mysql

Summary:	DataObjects MySQL Driver
Name:		rubygem-%{rbname}
Url:		http://rubygems.org/gems/do_mysql
Version:	0.10.14
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	mysql-devel

Requires:	rubygem(data_objects) = 0.10.14

%description
Implements the DataObjects API for MySQL.

%files
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/do_mysql/*.rb
%{ruby_sitearchdir}/%{rbname}/do_mysql.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------
%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.markdown
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE

#----------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install






