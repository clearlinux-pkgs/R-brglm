#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-brglm
Version  : 0.7.2
Release  : 54
URL      : https://cran.r-project.org/src/contrib/brglm_0.7.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/brglm_0.7.2.tar.gz
Summary  : Bias Reduction in Binomial-Response Generalized Linear Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-brglm-lib = %{version}-%{release}
Requires: R-profileModel
BuildRequires : R-profileModel
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-brglm package.
Group: Libraries

%description lib
lib components for the R-brglm package.


%prep
%setup -q -c -n brglm
cd %{_builddir}/brglm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640984256

%install
export SOURCE_DATE_EPOCH=1640984256
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brglm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brglm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brglm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc brglm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/brglm/CHANGES
/usr/lib64/R/library/brglm/CITATION
/usr/lib64/R/library/brglm/DESCRIPTION
/usr/lib64/R/library/brglm/INDEX
/usr/lib64/R/library/brglm/Jeffreys_power.R
/usr/lib64/R/library/brglm/Meta/Rd.rds
/usr/lib64/R/library/brglm/Meta/data.rds
/usr/lib64/R/library/brglm/Meta/features.rds
/usr/lib64/R/library/brglm/Meta/hsearch.rds
/usr/lib64/R/library/brglm/Meta/links.rds
/usr/lib64/R/library/brglm/Meta/nsInfo.rds
/usr/lib64/R/library/brglm/Meta/package.rds
/usr/lib64/R/library/brglm/NAMESPACE
/usr/lib64/R/library/brglm/R/brglm
/usr/lib64/R/library/brglm/R/brglm.rdb
/usr/lib64/R/library/brglm/R/brglm.rdx
/usr/lib64/R/library/brglm/WORDLIST
/usr/lib64/R/library/brglm/data/lizards.rda
/usr/lib64/R/library/brglm/help/AnIndex
/usr/lib64/R/library/brglm/help/aliases.rds
/usr/lib64/R/library/brglm/help/brglm.rdb
/usr/lib64/R/library/brglm/help/brglm.rdx
/usr/lib64/R/library/brglm/help/paths.rds
/usr/lib64/R/library/brglm/html/00Index.html
/usr/lib64/R/library/brglm/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/brglm/libs/brglm.so
/usr/lib64/R/library/brglm/libs/brglm.so.avx2
/usr/lib64/R/library/brglm/libs/brglm.so.avx512
