%define		docversion	1.77
Summary:	Modular DocBook Stylesheets
Summary(es):	Plantillas de estilo modulares de Norman Walsh para DocBook
Summary(pl):	Arkusze stylistyczne DSSSL dla DocBook DTD
Summary(pt_BR):	"stylesheets" modulares para o docbook, de Norman Walsh
Summary(ru):	Модульные стилевые шаблоны для DocBook от Norman Walsh
Summary(uk):	Модульн╕ стильов╕ шаблони для DocBook в╕д Norman Walsh
Name:		docbook-style-dsssl
Version:	1.78
Release:	1
License:	(C) 1997, 1998 Norman Walsh (Free)
Vendor:		Norman Walsh http://nwalsh.com/
Group:		Applications/Publishing/SGML
Source0:	http://dl.sourceforge.net/docbook/docbook-dsssl-%{version}.tar.gz
# Source0-md5: f60521a38bd425e76f50d3f15b0325c0
Source1:	docbook-dsssl-online.dsl
Source2:	http://dl.sourceforge.net/docbook/docbook-dsssl-doc-%{docversion}.tar.gz
# Source2-md5: d0b7a6ef410513dbd2a5f69457df0ac7
Patch1:		%{name}-articleinfo.patch
URL:		http://docbook.sourceforge.net/projects/dsssl/
Requires:	openjade
BuildRequires:	perl
Requires(post,postun):	sgml-common >= 0.5
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

rm -rf doc docsrc
mv -f  docbook-dsssl-%{docversion}/doc .
rm -rf docbook-dsssl-%{docversion}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets \
	$RPM_BUILD_ROOT%{_bindir}

cp -a * $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets
# docs are in standard place
rm -rf $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/doc

install %{SOURCE1} \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/contrib

perl -pe 's/^#.+?- Perl -.+?$/#\!\/usr\/bin\/perl/g' \
	bin/collateindex.pl > $RPM_BUILD_ROOT%{_bindir}/collateindex
	
cp bin/ChangeLog bin-ChangeLog

# shutup check-files
rm -f $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/BUGS \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/ChangeLog \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/README \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/TODO \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/WhatsNew \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/bin/ChangeLog \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/dsssl-stylesheets/bin/collateindex.pl

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 1.77-1
if ! grep -q /etc/sgml/dsssl-stylesheets.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/dsssl-stylesheets.cat %{_datadir}/sgml/docbook/dsssl-stylesheets/catalog > /dev/null
fi

%pre
if [ -L %{_datadir}/sgml/docbook/dsssl-stylesheets ] ; then
	rm -rf %{_datadir}/sgml/docbook/dsssl-stylesheets
fi

%post
if ! grep -q /etc/sgml/dsssl-stylesheets.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/dsssl-stylesheets.cat %{_datadir}/sgml/docbook/dsssl-stylesheets/catalog > /dev/null
fi

%postun
if [ "$1" = 0 ]; then
	/usr/bin/install-catalog --remove /etc/sgml/dsssl-stylesheets.cat %{_datadir}/sgml/docbook/dsssl-stylesheets/catalog > /dev/null
fi

%files
%defattr(644,root,root,755)
%doc doc ChangeLog WhatsNew BUGS TODO README bin-ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/sgml/docbook/dsssl-stylesheets
%{_datadir}/sgml/docbook/dsssl-stylesheets/VERSION
#%%{_datadir}/sgml/docbook/dsssl-stylesheets/bin
%{_datadir}/sgml/docbook/dsssl-stylesheets/catalog
%{_datadir}/sgml/docbook/dsssl-stylesheets/common
%{_datadir}/sgml/docbook/dsssl-stylesheets/contrib
#%%{_datadir}/sgml/docbook/dsssl-stylesheets/doc
#%%{_datadir}/sgml/docbook/dsssl-stylesheets/docsrc
%{_datadir}/sgml/docbook/dsssl-stylesheets/dtds
%{_datadir}/sgml/docbook/dsssl-stylesheets/frames
%{_datadir}/sgml/docbook/dsssl-stylesheets/html
%{_datadir}/sgml/docbook/dsssl-stylesheets/images
%{_datadir}/sgml/docbook/dsssl-stylesheets/lib
%{_datadir}/sgml/docbook/dsssl-stylesheets/olink
%{_datadir}/sgml/docbook/dsssl-stylesheets/print
