Here is the patch:

```java
public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    eu.europa.esig.dss.token.JKSSignatureToken signingToken = new eu.europa.esig.dss.token.JKSSignatureToken(keyStore, new java.security.KeyStore.PasswordProtection(keyStorePassword));
    log.debug("Keystore created for signing");
    eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
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
    signatureParameters.setPermission(eu.europa.esig.dss.enumerations.Permission.CERTIFICATION_NO_CHANGES_ALLOWED);
    eu.europa.esig.dss.validation.CommonCertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerifier();
    eu.europa.esig.dss.pades.signature.PAdESService service = new eu.europa.esig.dss.pades.signature.PAdESService(commonCertificateVerifier);
    log.debug("Signature service initialized");
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
        java.time.format.DateTimeFormatter formatter = java.time.format.DateTimeFormatter.ISO_OFFSET_DATE_TIME.withZone(java.time.ZoneId.systemDefault());
        if (params.getTimezone() != null) {
            formatter = formatter.withZone(java.time.ZoneId.of(params.getTimezone()));
        }
        fieldParameters.setSignatureDate(formatter.format(signatureParameters.getSigningDate().toInstant()));
        fieldParameters.setSignaturString(signingToken.getKey(keyAlias).getCertificate().getSubject().getPrettyPrintRFC2253());
        if (!com.beust.jcommander.Strings.isStringEmpty(params.getHint())) {
            fieldParameters.setHint(params.getHint());
        } else {
            fieldParameters.setHint(Configuration.getInstance().getResourceBundle().getString("hint_text"));
        }
        signatureParameters.setImageParameters(imageParameters);
        eu.europa.esig.dss.pdf.pdfbox.PdfBoxNativeObjectFactory pdfBoxNativeObjectFactory = new org.openpdfsign.dss.PdfBoxNativeTableObjectFactory();
        service.setPdfObjFactory(pdfBoxNativeObjectFactory);
        log.debug("Visible signature parameters set");
    }
    if (params.getUseTimestamp() || (params.getTSA() != null)) {
        eu.europa.esig.dss.spi.x509.tsp.CompositeTSPSource compositeTSPSource = new eu.europa.esig.dss.spi.x509.tsp.CompositeTSPSource();
        java.util.Map<java.lang.String, eu.europa.esig.dss.spi.x509.tsp.TSPSource> tspSources = new java.util.HashMap<>();
        compositeTSPSource.setTspSources(tspSources);
        if (params.getTSA().isEmpty()) {
            java.util.Arrays.stream(Configuration.getInstance().getProperties().getStringArray("tsp_sources")).forEach(( source) -> {
                tspSources.put(source, new eu.europa.esig.dss.service.tsp.OnlineTSPSource(source));
            });
        } else {
            params.getTSA().stream().forEach(( source) -> {
                tspSources.put(source, new eu.europa.esig.dss.service.tsp.OnlineTSPSource(source));
            });
        }
        service.setTspSource(compositeTSPSource);
    }
    ToBeSigned dataToSign = service.getDataToSign(toSignDocument, signatureParameters);
    eu.europa.esig.dss.enumerations.DigestAlgorithm digestAlgorithm = signatureParameters.getDigestAlgorithm();
    log.debug("Data to be signed loaded");
    SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));
    log.debug("Signature value calculated");
    DSSDocument signedDocument = service.signDocument(toSignDocument, signatureParameters, signatureValue);
    log.debug("Document signing complete");
    if (binary) {
        signedDocument.writeTo(java.lang.System.out);
    } else {
        signedDocument.save(outputFile.toAbsolutePath().toString());
    }
}
```