%define		docversion	1.75
Summary:	Modular DocBook Stylesheets
Summary(es):	Plantillas de estilo modulares de Norman Walsh para DocBook
Summary(pl):	Arkusze stylistyczne DSSSL dla DocBook DTD
Summary(pt_BR):	"stylesheets" modulares para o docbook, de Norman Walsh
Summary(ru):	Модульные стилевые шаблоны для DocBook от Norman Walsh
Summary(uk):	Модульн╕ стильов╕ шаблони для DocBook в╕д Norman Walsh
Name:		docbook-style-dsssl
Version:	1.76
Release:	8
License:	(C) 1997, 1998 Norman Walsh (Free)
Vendor:		Norman Walsh http://nwalsh.com/
Group:		Applications/Publishing/SGML
Source0:	http://prdownloads.sourceforge.net/docbook/docbook-dsssl-%{version}.tar.gz
Source1:	docbook-dsssl-online.dsl
Source2:	http://prdownloads.sourceforge.net/docbook/docbook-dsssl-doc-%{docversion}.tar.gz
Patch1:		%{name}-articleinfo.patch
Patch2:		%{name}-seealso.spec
URL:		http://docbook.sourceforge.net/projects/dsssl/
Requires:	openjade
BuildRequires:	perl
Requires(post):	sgml-common >= 0.5
Requires(postun):sgml-common
BuildArch:	noarch
AutoReqProv:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	stylesheets
Obsoletes:	docbook-dsssl

%description
DSSSL is a stylesheet language for both print and online rendering.
There is DSSSL stylesheets for DocBook DTD.

%description -l es
Plantillas de estilo DSSSL permiten convertir cualquier documento
Docbook en otro formato impreso (por ejemplo, RTF o PostScript) o en
lМnea (por ejemplo, HTML). иstos son altamente personalizables.

%description -l pl
docbook-dsssl jest zbiorem arkuszy stylistycznych pozwalaj╠cych
przeksztaЁciФ dokument napisany w DocBook DTD 3.0. na prezentacjЙ
on-line (wykorzystuj╠c HTML) lub na drukowany dokument (wykorzystuj╠c
jadetex lub RTF).

%description -l pt_BR
Estes stylesheets DSSSL permitem converter qualquer documento DocBook
para outro formato imprimМvel (por exemplo, RTF ou PostScript) ou
on-line (por exemplo, HTML). Eles sЦo altamente personalizАveis.

%description -l ru
Эти стилевые шаблоны DSSSL позволяют конвертировать любой DocBook
документ в другой онлайновый формат (например, HTML) или формат для
печати (например, RTF или PostScript).

%description -l uk
Ц╕ стильов╕ шаблони DSSSL дозволяють конвертувати будь-який DocBook
документ в ╕нший онлайновий формат (наприклад, HTML) чи формат для
друку (наприклад, RTF чи PostScript).

%prep
%setup -q -n docbook-dsssl-%{version} -a 2 
%patch1 -p1
%patch2 -p1

rm -rf doc docsrc
mv -f  docbook-dsssl-%{docversion}/doc .
rm -rf docbook-dsssl-%{docversion}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version} \
	$RPM_BUILD_ROOT%{_bindir}

cp -a * $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}
# docs are in standard place
rm -rf $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/doc

install %{SOURCE1} \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/contrib

perl -pe 's/^#.+?- Perl -.+?$/#\!\/usr\/bin\/perl/g' \
	bin/collateindex.pl > $RPM_BUILD_ROOT%{_bindir}/collateindex

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/install-catalog --add /etc/sgml/dsssl-stylesheets-%{version}-%{release}.cat %{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/catalog > /dev/null
ln -sfn dsssl-stylesheets-%{version} %{_datadir}/sgml/docbook/dsssl-stylesheets

%postun
/usr/bin/install-catalog --remove /etc/sgml/dsssl-stylesheets-%{version}-%{release}.cat %{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/catalog > /dev/null
if [ "$1" = 0 ]; then
	rm -f %{_datadir}/sgml/docbook/dsssl-stylesheets
fi

%files
%defattr(644,root,root,755)
%doc doc ChangeLog WhatsNew BUGS TODO README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/VERSION
#%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/bin
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/catalog
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/common
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/contrib
#%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/doc
#%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/docsrc
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/dtds
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/frames
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/html
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/images
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/lib
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/olink
%{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}/print
