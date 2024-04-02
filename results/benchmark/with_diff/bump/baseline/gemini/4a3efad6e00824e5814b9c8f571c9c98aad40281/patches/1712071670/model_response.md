```java
import eu.europa.esig.dss.pades.PAdESSigner;
import eu.europa.esig.dss.pades.signature.SignaturePackaging;
import eu.europa.esig.dss.pades.signature.SignaturePackaging.SignaturePackagingBuilder;

public class Signer {

  public static void main(String[] args) throws Exception {
    // create a new PAdESSigner instance
    PAdESSigner signer = new PAdESSigner();

    // create a new SignaturePackagingBuilder instance
    SignaturePackagingBuilder builder = SignaturePackaging.builder();

    // set the signature packaging options
    builder.withSignaturePackaging(SignaturePackaging.SignaturePackagingEnum.ENVELOPED);

    // create the signature packaging
    SignaturePackaging signaturePackaging = builder.build();

    // sign the document
    signer.signDocument(signaturePackaging, null, null);
  }
}
```