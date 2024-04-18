It looks like the `CertificationPermission` class is missing from the code. Here's a possible patch to fix the error:
```diff
- signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
+ signatureParameters.setPermission(new org.openpdfsign.permission.CertificationPermission(org.openpdfsign.permission.CertificationPermission.MINIMAL_CHANGES_PERMITTED));
```
This patch creates a new instance of the `CertificationPermission` class with the `MINIMAL_CHANGES_PERMITTED` constant, which should fix the error.

Here's the full patched code:
```java
public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    // https://github.com/apache/pdfbox/blob/trunk/examples/src/main/java/org/apache/pdfbox/examples/signature/CreateVisibleSignature2.java
    // https://ec.europa.eu/cefdigital/DSS/webapp-demo/doc/dss-documentation.html
    // load PDF file
    // PDDocument doc = PDDocument.load(pdfFile.toFile());
    // load PDF file in DSSDocument format
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    // load certificate and private key
    eu.europa.esig.dss.token.JKSSignatureToken signingToken = new eu.europa.esig.dss.token.JKSSignatureToken(keyStore, new java.security.KeyStore.PasswordProtection(keyStorePassword));
    log.debug("Keystore created for signing");
    // PAdES parameters
    eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
    // signatureParameters.bLevel().setSigningDate(new Date());
    java.lang.String keyAlias = "alias";
    if (signingToken.getKeys().get(0) instanceof eu.europa.esig.dss.token.KSPrivateKeyEntry) {
        keyAlias = ((eu.europa.esig.dss.token.KSPrivateKeyEntry) (signingToken.getKeys().get(0))).getAlias();
    }
    signatureParameters.setSigningCertificate(signingToken.getKey(keyAlias).getCertificate());
    signatureParameters.setCertificateChain(signingToken.getKey(keyAlias).getCertificateChain());
    if (params.getUseTimestamp() || (!params.getTSA().isEmpty())) {
        signatureParameters.setSignatureLevel(eu.europa.esig.dss.enumerations.SignatureLevel.PAdES_BASELINE_T);
    } else {
        signatureParameters.setSignatureLevel(eu.europa.esig.dss.enumerations.SignatureLevel.PAdES_BASELINE_B);
    }
    signatureParameters.setPermission(new org.openpdfsign.permission.CertificationPermission(org.openpdfsign.permission.CertificationPermission.MINIMAL_CHANGES_PERMITTED));
    // Create common certificate verifier
    eu.europa.esig.dss.validation.CommonCertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerifier();
    // Create PAdESService for signature
    eu.europa.esig.dss.pades.signature.PAdESService service = new eu.europa.esig.dss.pades.signature.PAdESService(commonCertificateVerifier);
    log.debug("Signature service initialized");
    // Initialize visual signature and configure
    if (visibleSignature) {
        eu.europa.esig.dss.pades.SignatureImageParameters imageParameters = new eu.europa.esig.dss.pades.SignatureImageParameters();
        TableSignatureFieldParameters fieldParameters = new TableSignatureFieldParameters();
        imageParameters.setFieldParameters(fieldParameters);
        if (!com.beust.jcommander.Strings.isStringEmpty(params.getImageFile())) {
            imageParameters.setImage(new InMemoryDocument(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(params.getImageFile()))));
        } else {
            imageParameters.setImage(new InMemoryDocument(org.apache.commons.io.IOUtils.toByteArray(getClass().getClassLoader().getResourceAsStream("signature.png"))));
        }
        if (params.getPage() < 0) {
            org.apache.pdfbox.pdmodel.PDDocument pdDocument = org.apache.pdfbox.pdmodel.PDDocument.load(toSignDocument.openStream());
            int pageCount = pdDocument.getNumberOfPages();
            fieldParameters.setPage(pageCount + (1 + params.getPage()));
            pdDocument.close();
            log.debug("PDF page count: " + pageCount);
        } else {
            fieldParameters.setPage(params.getPage());
        }
        fieldParameters.setOriginX((params.getLeft() * org.openpdfsign.Signer.POINTS_PER_MM) * 10.0F);
        fieldParameters.setOriginY((params.getTop() * org.openpdfsign.Signer.POINTS_PER_MM) * 10.0F);
        fieldParameters.setWidth((params.getWidth() * org.openpdfsign.Signer.POINTS_PER_MM) * 10.0F);
        // Get the SignedInfo segment that need to be signed.
        // respect local timezone
        java.time.format.DateTimeFormatter formatter = java.time.format.DateTimeFormatter.ISO_OFFSET_DATE_TIME.withZone(java.time.ZoneId.systemDefault());
        // user-provided timezone, if any
        if (params.getTimezone() != null) {
            formatter