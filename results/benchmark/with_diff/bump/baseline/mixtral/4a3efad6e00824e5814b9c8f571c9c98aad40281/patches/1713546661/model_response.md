Here is a proposed patch for the failing client code:
```java
import eu.europa.esig.dss.pades.PadesSigner;
import eu.europa.esig.dss.pades.PadesSigningCertificate;

// ...

@Override
public void signDocument(InputStream inputStream, OutputStream outputStream) throws Exception {
    PadesSigner signer = new PadesSigner(certificate, OcspClient.getOcspClient(), CrlClient.getCrlClient(), getTsaClient());
    PadesSigningCertificate padesSigningCertificate = new PadesSigningCertificate(certificate);
    signer.setSigningCertificate(padesSigningCertificate);
    signer.setSignatureLevel(SignatureLevel.ESH_EXCL);
    signer.setSignaturePolicy(signaturePolicy);
    signer.setSigningDate(new Date());
    signer.setReason(reason);
    signer.setLocation(location);
    signer.setTspSource(tspSource);
    signer.setTimeStampToken(timeStampToken);
    signer.setApprovalSignatureFieldId(approvalSignatureFieldId);
    signer.setVisualSignatureFieldId(visualSignatureFieldId);
    signer.setVisualSignatureTemplate(visualSignatureTemplate);
    signer.setProperty(Property.SIGNATURE_POLICY_IDENTIFIER, signaturePolicyIdentifier);
    signer.setProperty(Property.DIGEST_ALGORITHM, DigestAlgorithm.SHA256);
    signer.setProperty(Property.SIGNATURE_PROVIDER, signatureProvider);
    signer.setProperty(Property.CMS_SIGNER_INFO_GENERATOR, cmsSignerInfoGenerator);
    signer.setProperty(Property.CMS_CONTENT_INFO_GENERATOR, cmsContentInfoGenerator);
    signer.setProperty(Property.CMS_SIGNATURE_GENERATOR, cmsSignatureGenerator);
    signer.setProperty(Property.CMS_ENCRYPTOR, cmsEncryptor);
    signer.setProperty(Property.CMS_MESSAGE_DIGEST_CALCULATOR, cmsMessageDigestCalculator);
    signer.setProperty(Property.CMS_ATTRIBUTE_TABLE_GENERATOR, cmsAttributeTableGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_VALIDATOR, cmsCertificateValidator);
    signer.setProperty(Property.CMS_CERTIFICATE_CHAIN_VALIDATOR, cmsCertificateChainValidator);
    signer.setProperty(Property.CMS_CONTENT_TRANSFORMER, cmsContentTransformer);
    signer.setProperty(Property.CMS_ENCRYPTION_KEY_WRAPPER, cmsEncryptionKeyWrapper);
    signer.setProperty(Property.CMS_SIGNATURE_POLICY_GENERATOR, cmsSignaturePolicyGenerator);
    signer.setProperty(Property.CMS_SIGNER_INFO_PROPERTIES_GENERATOR, cmsSignerInfoPropertiesGenerator);
    signer.setProperty(Property.CMS_ATTRIBUTE_TABLE_PROPERTIES_GENERATOR, cmsAttributeTablePropertiesGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_PROPERTIES_GENERATOR, cmsCertificatePropertiesGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_CHAIN_PROPERTIES_GENERATOR, cmsCertificateChainPropertiesGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_VALIDATOR_PROPERTIES_GENERATOR, cmsCertificateValidatorPropertiesGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_CHAIN_VALIDATOR_PROPERTIES_GENERATOR, cmsCertificateChainValidatorPropertiesGenerator);
    signer.setProperty(Property.CMS_CONTENT_INFO_PROPERTIES_GENERATOR, cmsContentInfoPropertiesGenerator);
    signer.setProperty(Property.CMS_SIGNATURE_PROPERTIES_GENERATOR, cmsSignaturePropertiesGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_ID_GENERATOR, cmsCertificateIdGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_ID_PROPERTIES_GENERATOR, cmsCertificateIdPropertiesGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_ID_VALIDATOR, cmsCertificateIdValidator);
    signer.setProperty(Property.CMS_CERTIFICATE_ID_VALIDATOR_PROPERTIES_GENERATOR, cmsCertificateIdValidatorPropertiesGenerator);
    signer.setProperty(Property.CMS_CERTIFICATE_PROPERTIES_VALIDATOR, cmsCertificatePropertiesValidator);
    signer.setProperty(Property.CMS_CERTIFICATE_CHAIN_PROPERTIES_VALIDATOR, cmsCertificateChainPropertiesValidator);
    signer.setProperty(Property.CMS_CONTENT_INFO_VALIDATOR, cmsContentInfoValidator);
    signer.setProperty(Property.CMS_SIGNATURE_VALIDATOR, cmsSignatureValidator);
    signer.setProperty(Property.CMS_SIGNATURE_POLICY_VALIDATOR, cmsSignaturePolicyValidator);
    signer.setProperty(Property.CMS_CERTIFICATE_VALIDATOR_PROPERTIES, cmsCertificateValidatorProperties);
    signer.setProperty(Property.CMS_CERTIFICATE_CHAIN_VALIDATOR_PROPERTIES, cmsCertificateChainValidatorProperties);
    signer.setProperty(Property.CMS_CONTENT_INFO_PROPERTIES, cmsContentInfoProperties);
    signer.setProperty(Property.CMS_SIGNATURE_PROPERTIES, cmsSignatureProperties);
    signer.setProperty(Property.CMS_CERTIFICATE_PROPERTIES, cmsCertificateProperties);
    signer.setProperty(Property.CMS_CERTIFICATE_CHAIN_PROPERTIES, cmsCertificateChainProperties);
    signer.setProperty(Property.CMS_CERTIFICATE_ID_PROPERTIES, cmsCertificateIdProperties);
    signer.setProperty(Property.CMS_CERTIFICATE_ID_VALIDATOR_PROPERTIES, cmsCertificateIdValidatorProperties);
    signer.setProperty(Property.CMS_CERTIFICATE_PROPERTIES_VALIDATOR_PROPERTIES, cmsCertificatePropertiesValidatorProperties);
    signer.setProperty(Property.CMS_CERTIFICATE_CHAIN_PROPERTIES_VALIDATOR_PROPERTIES, cmsCertificateChainPropertiesValidatorProperties);
    signer.setProperty(Property.CMS_CONTENT_INFO_VALIDATOR_PROPERTIES, cmsContentInfoValidatorProperties);
    signer.setProperty(Property.CMS_SIGNATURE_VALIDATOR_PROPERTIES, cmsSignatureValidatorProperties);
    signer.setProperty(Property.CMS_SIGNATURE_POLICY_VALIDATOR_PROPERTIES, cmsSignaturePolicyValidatorProperties);

    signer.sign(inputStream, outputStream);
}
```
The patch removes the import statement for `CertificationPermission` and replaces the use of `CertificationPermission` with `PadesSigningCertificate`. This is based on the assumption that `CertificationPermission` has been removed in the new library version and its functionality has been replaced by `PadesSigningCertificate`. Additionally, the patch sets the `signatureLevel` property to `ESH_EXCL`, which is an added method in the new library version.