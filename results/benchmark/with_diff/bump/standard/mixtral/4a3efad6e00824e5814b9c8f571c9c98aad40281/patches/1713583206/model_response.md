Here's the updated code with the required changes:

`import eu.europa.esig.dss.pades.CertificationPermission;`

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
**CertificationPermission minimalCertificationPermission = new CertificationPermission(CertificationPermission.DIGITAL_SIGNATURE);**
signatureParameters.setPermission(minimalCertificationPermission);
// Create common certificate verifier
eu.europa.esig.dss.validation.CommonCertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerifier();
// Create PAdESService for signature
eu.europa.esig.dss.pades.signature.PAdESService service = new eu.europa.esig.dss.pades.signature.PAdESService(commonCertificateVerifier);
log.debug("Signature service initialized");
// Initialize visual signature and configure
if (visibleSignature) {
// ... (rest of the code remains unchanged)
}
// ... (rest of the code remains unchanged)
}