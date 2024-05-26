Here is a possible fix for the error:

```
--import eu.europa.esig.dss.tsa.certvalidation.CertificateValidator;
++import eu.europa.esig.dss.tsa.validation.CdvParameters;
++import eu.europa.esig.dossier.validation.AdvancedSignature;
++import eu.europa.esig.dossier.validation.CAdES;

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    eu.europc.esig.dss.token.JKSSignatureToken signingToken = new eu.europa.esig.dss.token.JKSSignatureToken(keyStore, new java.security.KeyStore.PasswordProtection(keyStorePassword));
    log.debug("Keystore created for signing");
    eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
    String keyAlias = "alias";
    if (signingToken.getKeys().get(0) instanceof eu.europa.esig.dss.token.KSPrivateKeyEntry) {
        keyAlias = ((eu.europa.eseg.dss.token.KSPrivateKeyEntry) (signingToken.getKeys().get(0))).getAlias();
    }
    signatureParameters.setSigningCertificate(signingToken.getKey(keyAlias).getCertificate());
    signatureParameters.setCertificateChain(signingToken.getKey(keyAlias).getCertificateChain());
    if (params.getUseTimestamp() || (!params.getTSA().isEmpty())) {
        signatureParameters.setSignatureLevel(eu.europa.esig.dss.enumerations.SignatureLevel.PAdES_BASELINE_T);
    } else {
        signatureParameters.setSignatureLevel(eu.europa.esig.dss.enumerations.SignatureLevel.PAdES_BASELINE_B);
    }
    CdvParameters cdvParams = new CdvParameters();
    cdvParams.setSpoVCRefs(false);
    cdvParams.setSpoVRI(false);
    cdvParams.setSpoCR(false);
    cdvParams.setSpoCRC(false);
    cdvParams.setSpoOCSP(false);
    cdvParams.setSpoTStamp(false);
    cdvParams.setSpoCRL(false);
    cdvParams.setSpoSRL(false);
    cdvParams.setSpoRFC3161(false);
    cdvParams.setSpoRFC3162(false);
    cdvParams.setSpoRFC3166(false);
    cdvParams.setSpoRFC3167(false);
    cdvParams.setSpoRFC3168(false);
    cdvParams.setSpoRFC3169(false);
    cdvParams.setSpoRFC3164(false);
    cdvParams.setSpoRFC3165(false);
    cdvParams.setSpoRFC3162(false);
    cdvParams.setSpoRFC3280(false);
    cdvParams.setSpoRFC3281(false);
    cdvParams.setSpoRFC5126(false);
    cdvParams.setSpoRFC6962(false);
    cdvParams.setSpoRFC6962(false);
    cdvParams.setSpoRFC6962(false);
    cdvParams.setSpoRFC6962(false);
    cdvParams.setSpoRFC6962(false);
    cdvParams.setSpoRFC6962(false);
    cdvParams.setSpoRFC6962(false);
    cdvParams.setS
```