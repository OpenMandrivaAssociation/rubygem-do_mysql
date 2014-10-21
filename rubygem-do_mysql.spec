# Generated from do_mysql-0.10.7.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	do_mysql

Summary:	DataObjects MySQL Driver
Name:		rubygem-%{rbname}
Url:		http://rubygems.org/gems/do_mysql
Version:	0.10.14
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
Source0:	http://gems.rubyforge.org/gems/do_mysql-0.10.14.gem
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
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/ChangeLog_markdown.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/DataObjects.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/DataObjects/Mysql.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/DataObjects/Mysql/Connection.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/DataObjects/Mysql/Encoding.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/DataObjects/Mysql/Transaction.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/Jdbc.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/LICENSE.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/Object.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/README_markdown.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/fonts.css
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/fonts/Lato-Light.ttf
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/fonts/Lato-LightItalic.ttf
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/fonts/Lato-Regular.ttf
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/fonts/Lato-RegularItalic.ttf
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/fonts/SourceCodePro-Bold.ttf
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/fonts/SourceCodePro-Regular.ttf
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/add.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/arrow_up.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/brick.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/brick_link.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/bug.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/bullet_black.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/bullet_toggle_minus.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/bullet_toggle_plus.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/date.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/delete.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/find.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/loadingAnimation.gif
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/macFFBgHack.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/package.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/page_green.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/page_white_text.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/page_white_width.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/plugin.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/ruby.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/tag_blue.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/tag_green.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/transparent.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/wrench.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/wrench_orange.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/images/zoom.png
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/index.html
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/js/darkfish.js
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/js/jquery.js
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/js/navigation.js
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/js/search.js
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/js/search_index.js
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/js/searcher.js
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/rdoc.css
%{_datadir}/gems/doc/do_mysql-0.10.14/rdoc/table_of_contents.html
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/Connection/cdesc-Connection.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/Encoding/cdesc-Encoding.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/Transaction/begin_prepared-i.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/Transaction/cdesc-Transaction.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/Transaction/commit_prepared-i.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/Transaction/finalize_transaction-i.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/Transaction/prepare-i.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/Transaction/rollback_prepared-i.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/Mysql/cdesc-Mysql.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/DataObjects/cdesc-DataObjects.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/Jdbc/cdesc-Jdbc.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/Object/cdesc-Object.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/Object/secure%3f-i.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/Object/using_socket%3f-i.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/cache.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/page-ChangeLog_markdown.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/page-LICENSE.ri
%{_datadir}/gems/doc/do_mysql-0.10.14/ri/page-README_markdown.ri
%{_datadir}/gems/gems/do_mysql-0.10.14/ChangeLog.markdown
%{_datadir}/gems/gems/do_mysql-0.10.14/LICENSE
%{_datadir}/gems/gems/do_mysql-0.10.14/README.markdown
%{_datadir}/gems/gems/do_mysql-0.10.14/lib/do_mysql.rb
%{_datadir}/gems/gems/do_mysql-0.10.14/lib/do_mysql/encoding.rb
%{_datadir}/gems/gems/do_mysql-0.10.14/lib/do_mysql/transaction.rb
%{_datadir}/gems/gems/do_mysql-0.10.14/lib/do_mysql/version.rb
%{_datadir}/gems/specifications/do_mysql-0.10.14.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.markdown
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
