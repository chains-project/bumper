Here's the proposed patch:

Replace the failing line with the following code segment:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.certificate.CertificateToken;
import eu.europa.esig.dss.pades.certificate.CertificateVerifier;
import eu.europa.esig.dss.pades.tsa.TSPSource;
import eu.europa.esig.dss.pades.tsa.TimeStampTokenProvider;
import eu.europa.esig.dss.pades.tsa.TspSource;
import eu.europa.esig.dss.pades.tsa.TspSourceFactory;
import eu.europa.esig.dss.pades.validation.PAdESValidationDataProvider;
import eu.europa.esig.dss.pades.validation.PAdESValidationService;
import eu.europa.esig.dss.pades.validation.reports.PAdESReport;
import eu.europa.esig.dss.token.DSSPrivateKeyEntry;
import eu.europa.esig.dss.token.DSSPublicKeyEntry;
import eu.europa.esig.dss.validation.CertificateVerifierProvider;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.validation.SignedDocumentValidator;
import eu.europa.esig.dss.validation.reports.Reports;
import eu.europa.esig.dss.validation.reports.SimpleReport;
import eu.europa.esig.dss.validation.reports.SubReport;
import eu.europa.esig.dss.validation.reports.Trace;
import eu.europa.esig.dss.validation.reports.ValidationReport;
import eu.europa.esig.dss.validation.reports.jaxb.XmlAdESReport;
import eu.europa.esig.dss.validation.reports.jaxb.XmlCertificate;
import eu.europa.esig.dss.validation.reports.jaxb.XmlCertificateRefBy;
import eu.europa.esig.dss.validation.reports.jaxb.XmlCertificateRefs;
import eu.europa.esig.dss.validation.reports.jaxb.XmlCertificateToken;
import eu.europa.esig.dss.validation.reports.jaxb.XmlContainedCertificate;
import eu.europa.esig.dss.validation.reports.jaxb.XmlDetachedSignature;
import eu.europa.esig.dss.validation.reports.jaxb.XmlDocument;
import eu.europa.esig.dss.validation.reports.jaxb.XmlError;
import eu.europa.esig.dss.validation.reports.jaxb.XmlErrorDetails;
import eu.europa.esig.dss.validation.reports.jaxb.XmlInfo;
import eu.europa.esig.dss.validation.reports.jaxb.XmlMessage;
import eu.europa.esig.dss.validation.reports.jaxb.XmlMessageDetails;
import eu.europa.esig.dss.validation.reports.jaxb.XmlOcspResponse;
import eu.europa.esig.dss.validation.reports.jaxb.XmlRevocationRefs;
import eu.europa.esig.dss.validation.reports.jaxb.XmlRevocationReason;
import eu.europa.esig.dss.validation.reports.jaxb.XmlRevocationTime;
import eu.europa.esig.dss.validation.reports.jaxb.XmlSignatures;
import eu.europa.esig.dss.validation.reports.jaxb.XmlSignedData;
import eu.europa.esig.dss.validation.reports.jaxb.XmlSigningCertificate;
import eu.europa.esig.dss.validation.reports.jaxb.XmlTimestamp;
import eu.europa.esig.dss.validation.reports.jaxb.XmlTspResponse;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationProcess;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTime;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetails;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSimple;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReport;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSimple;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReport;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSimple;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSubReport;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSubReportSimple;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSubReportSubReport;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSubReportSubReportSimple;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSubReportSubReportSubReport;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSubReportSubReportSubReport;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSubReportSubReportSubReportSimple;
import eu.europa.esig.dss.validation.reports.jaxb.XmlValidationTimeDetailsSubReportSubReportSubReportSubReportSubReportSubReport;

// ...

signatureParameters.setPermission(new PAdESSignatureParameters.Permission(PAdESSignatureParameters.Permission.PermissionElement.MINIMAL_CHANGES_PERMITTED));
```

This patch uses the `PAdESSignatureParameters.Permission` class instead of the removed `CertificationPermission` enum. The permission is initialized with the `PAdESSignatureParameters.PermissionElement.MINIMAL_CHANGES_PERMITTED` constant.