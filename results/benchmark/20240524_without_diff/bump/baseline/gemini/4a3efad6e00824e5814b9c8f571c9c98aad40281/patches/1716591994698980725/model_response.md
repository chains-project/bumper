```java
import eu.europa.esig.dss.pades.CertificationPermission;
import eu.europa.esig.dss.pades.PAdESService;
import eu.europa.esig.dss.spi.DSSUtils;
import org.bouncycastle.cms.CMSSignedData;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.security.Security;
import java.security.cert.Certificate;
import java.security.cert.X509Certificate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

public class Signer {

    private static final String BC = BouncyCastleProvider.PROVIDER_NAME;

    static {
        Security.addProvider(new BouncyCastleProvider());
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, CertificationPermission permission) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, CertificationPermission permission) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, byte[] externalSigningCertificate, String externalSigningCertificatePassword) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, externalSigningCertificate, externalSigningCertificatePassword);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, byte[] externalSigningCertificate, String externalSigningCertificatePassword) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, externalSigningCertificate, externalSigningCertificatePassword);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, CertificationPermission permission, byte[] externalSigningCertificate, String externalSigningCertificatePassword) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, externalSigningCertificate, externalSigningCertificatePassword);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, CertificationPermission permission, byte[] externalSigningCertificate, String externalSigningCertificatePassword) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, externalSigningCertificate, externalSigningCertificatePassword);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, byte[] externalSigningCertificate, String externalSigningCertificatePassword, String tsaUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, externalSigningCertificate, externalSigningCertificatePassword, tsaUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, byte[] externalSigningCertificate, String externalSigningCertificatePassword, String tsaUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, externalSigningCertificate, externalSigningCertificatePassword, tsaUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, CertificationPermission permission, byte[] externalSigningCertificate, String externalSigningCertificatePassword, String tsaUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, externalSigningCertificate, externalSigningCertificatePassword, tsaUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, CertificationPermission permission, byte[] externalSigningCertificate, String externalSigningCertificatePassword, String tsaUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, externalSigningCertificate, externalSigningCertificatePassword, tsaUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, String tsaUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, tsaUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, String tsaUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, tsaUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, CertificationPermission permission, String tsaUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, tsaUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, CertificationPermission permission, String tsaUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, tsaUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, byte[] externalSigningCertificate, String externalSigningCertificatePassword, String tsaUrl, String ocspUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, externalSigningCertificate, externalSigningCertificatePassword, tsaUrl, ocspUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, byte[] externalSigningCertificate, String externalSigningCertificatePassword, String tsaUrl, String ocspUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, externalSigningCertificate, externalSigningCertificatePassword, tsaUrl, ocspUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, CertificationPermission permission, byte[] externalSigningCertificate, String externalSigningCertificatePassword, String tsaUrl, String ocspUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, externalSigningCertificate, externalSigningCertificatePassword, tsaUrl, ocspUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, CertificationPermission permission, byte[] externalSigningCertificate, String externalSigningCertificatePassword, String tsaUrl, String ocspUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, externalSigningCertificate, externalSigningCertificatePassword, tsaUrl, ocspUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, String tsaUrl, String ocspUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, tsaUrl, ocspUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, String tsaUrl, String ocspUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, tsaUrl, ocspUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, CertificationPermission permission, String tsaUrl, String ocspUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, tsaUrl, ocspUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, CertificationPermission permission, String tsaUrl, String ocspUrl) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, tsaUrl, ocspUrl);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, String tsaUrl, String ocspUrl, String signingProfile) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, tsaUrl, ocspUrl, signingProfile);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, String tsaUrl, String ocspUrl, String signingProfile) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, null, tsaUrl, ocspUrl, signingProfile);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, X509Certificate certificate, String signatureAlgorithm, CertificationPermission permission, String tsaUrl, String ocspUrl, String signingProfile) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

        // Create a list of certificates to be included in the signature
        List<Certificate> certificates = new ArrayList<>();
        certificates.add(certificate);

        // Create a CMS SignedData object from the content and certificates
        CMSSignedData cmsSignedData = padesService.sign(content, certificates, permission, tsaUrl, ocspUrl, signingProfile);

        // Encode the CMS SignedData object to a byte array
        return cmsSignedData.getEncoded();
    }

    public static byte[] sign(byte[] content, Collection<X509Certificate> certificates, String signatureAlgorithm, CertificationPermission permission, String tsaUrl, String ocspUrl, String signingProfile) throws Exception {
        // Create a PAdES service with the desired signature algorithm
        PAdESService padesService = new PAdESService(signatureAlgorithm);

