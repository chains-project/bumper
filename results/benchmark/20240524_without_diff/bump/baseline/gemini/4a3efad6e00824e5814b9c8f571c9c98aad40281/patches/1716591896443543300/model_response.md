```java
import eu.europa.esig.dss.pades.CertificationPermission;

public class Signer {

    public void sign(byte[] data) {
        // Sign the data
        byte[] signature = signData(data);

        // Create a PAdES signature
        PAdESSignature signature1 = new PAdESSignature();
        signature1.setSignature(signature);

        // Add the signature to the PDF file
        PDFSigner signer = new PDFSigner();
        signer.signDetached(new ByteArrayInputStream(data), new ByteArrayOutputStream(), signature1, new CertificationPermission());
    }

    private byte[] signData(byte[] data) {
        // Sign the data using a private key
        Signature signature = Signature.getInstance("SHA256withRSA");
        signature.initSign(privateKey);
        signature.update(data);
        return signature.sign();
    }
}
```