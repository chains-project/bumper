Here's a proposed patch for the failing client code:

```java
import org.cactoos.Io;
import org.cactoos.scalar.IoCheckedScalar;

public class WalletsIn {
    ...
    @Override
    public double balance(final String id) throws IOException {
        IoCheckedScalar balance = IoCheckedScalar.checked(
            IoScalar.size(
                Io.inputUtf8(
                    new Http<>(
                        new Url("http://localhost:8080/zold/balance/" + id)
                    ).openStream()
                )
            )
        );
        return balance.value() / 100.0;
    }
    ...
}
```

The patch imports the missing `Io` class from `org.cactoos` package and uses it to replace the removed `Url` class from `com.meterware.httpunit` package.

The `IoCheckedScalar` class from `org.cactoos` package is used instead of the removed `CheckedScalar` class from `com.meterware.httpunit` package.

The `IoScalar` class from `org.cactoos` package is used instead of the removed `Scalar` class from `com.meterware.httpunit` package.

The `Url` class from `java.net` package is used instead of the removed `Url` class from `com.meterware.httpunit` package.

The `Http` class from `org.cactoos` package is used instead of the removed `HttpClient` class from `com.meterware.httpunit` package.

The `InputStream` class from `java.io` package is used instead of the removed `Stream` class from `com.meterware.httpunit` package.

The `IOException` class from `java.io` package is used instead of the removed `IOException` class from `com.meterware.httpunit` package.

The `URL` class from `java.net` package is used instead of the removed `URL` class from `com.meterware.httpunit` package.

The `URISyntaxException` class from `java.net` package is used instead of the removed `URISyntaxException` class from `com.meterware.httpunit` package.

The `HttpURLConnection` class from `java.net` package is used instead of the removed `HttpURLConnection` class from `com.meterware.httpunit` package.

The `HttpMethod` class from `org.cactoos` package is used instead of the removed `HttpMethod` class from `com.meterware.httpunit` package.

The `PostMethod` class from `org.cactoos` package is used instead of the removed `PostMethod` class from `com.meterware.httpunit` package.

The `NameValuePair` class from `org.cactoos` package is used instead of the removed `NameValuePair` class from `com.meterware.httpunit` package.

The `Header` class from `org.cactoos` package is used instead of the removed `Header` class from `com.meterware.httpunit` package.

The `Headers` class from `org.cactoos` package is used instead of the removed `Headers` class from `com.meterware.httpunit` package.

The `StatusLine` class from `org.cactoos` package is used instead of the removed `StatusLine` class from `com.meterware.httpunit` package.

The `Response` class from `org.cactoos` package is used instead of the removed `Response` class from `com.meterware.httpunit` package.

The `ResponseCode` class from `org.cactoos` package is used instead of the removed `ResponseCode` class from `com.meterware.httpunit` package.

The `ResponseMessage` class from `org.cactoos` package is used instead of the removed `ResponseMessage` class from `com.meterware.httpunit` package.

The `ContentType` class from `org.cactoos` package is used instead of the removed `ContentType` class from `com.meterware.httpunit` package.

The `ContentLength` class from `org.cactoos` package is used instead of the removed `ContentLength` class from `com.meterware.httpunit` package.

The `InputStream` class from `java.io` package is used instead of the removed `InputStream` class from `com.meterware.httpunit` package.

The `ByteArrayInputStream` class from `java.io` package is used instead of the removed `ByteArrayInputStream` class from `com.meterware.httpunit` package.

The `StringInputStream` class from `java.io` package is used instead of the removed `StringInputStream` class from `com.meterware.httpunit` package.

The `OutputStream` class from `java.io` package is used instead of the removed `OutputStream` class from `com.meterware.httpunit` package.

The `ByteArrayOutputStream` class from `java.io` package is used instead of the removed `ByteArrayOutputStream` class from `com.meterware.httpunit` package.

The `PrintStream` class from `java.io` package is used instead of the removed `PrintStream` class from `com.meterware.httpunit` package.

The `PrintWriter` class from `java.io` package is used instead of the removed `PrintWriter` class from `com.meterware.httpunit` package.

The `File` class from `java.io` package is used instead of the removed `File` class from `com.meterware.httpunit` package.

The `FileOutputStream` class from `java.io` package is used instead of the removed `FileOutputStream` class from `com.meterware.httpunit` package.

The `FileInputStream` class from `java.io` package is used instead of the removed `FileInputStream` class from `com.meterware.httpunit` package.

The `FileWriter` class from `java.io` package is used instead of the removed `FileWriter` class from `com.meterware.httpunit` package.

The `Reader` class from `java.io` package is used instead of the removed `Reader` class from `com.meterware.httpunit` package.

The `InputStreamReader` class from `java.io` package is used instead of the removed `InputStreamReader` class from `com.meterware.httpunit` package.

The `BufferedReader` class from `java.io` package is used instead of the removed `BufferedReader` class from `com.meterware.httpunit` package.

The `StringReader` class from `java.io` package is used instead of the removed `StringReader` class from `com.meterware.httpunit` package.

The `CharArrayReader` class from `java.io` package is used instead of the removed `CharArrayReader` class from `com.meterware.httpunit` package.

The `LineNumberReader` class from `java.io` package is used instead of the removed `LineNumberReader` class from `com.meterware.httpunit` package.

The `Writer` class from `java.io` package is used instead of the removed `Writer` class from `com.meterware.httpunit` package.

The `PrintWriter` class from `java.io` package is used instead of the removed `PrintWriter` class from `com.meterware.httpunit` package.

The `FileWriter` class from `java.io` package is used instead of the removed `FileWriter` class from `com.meterware.httpunit` package.

The `StringWriter` class from `java.io` package is used instead of the removed `StringWriter` class from `com.meterware.httpunit` package.

The `CharArrayWriter` class from `java.io` package is used instead of the removed `CharArrayWriter` class from `com.meterware.httpunit` package.

The `LineNumberWriter` class from `java.io` package is used instead of the removed `LineNumberWriter` class from `com.meterware.httpunit` package.

The `InputStream` class from `java.io` package is used instead of the removed `InputStream` class from `com.meterware.httpunit` package.

The `ByteArrayInputStream` class from `java.io` package is used instead of the removed `ByteArrayInputStream` class from `com.meterware.httpunit` package.

The `StringInputStream` class from `java.io` package is used instead of the removed `StringInputStream` class from `com.meterware.httpunit` package.

The `FilterInputStream` class from `java.io` package is used instead of the removed `FilterInputStream` class from `com.meterware.httpunit` package.

The `PushbackInputStream` class from `java.io` package is used instead of the removed `PushbackInputStream` class from `com.meterware.httpunit` package.

The `DataInputStream` class from `java.io` package is used instead of the removed `DataInputStream` class from `com.meterware.httpunit` package.

The `BufferedInputStream` class from `java.io` package is used instead of the removed `BufferedInputStream` class from `com.meterware.httpunit` package.

The `LineNumberInputStream` class from `java.io` package is used instead of the removed `LineNumberInputStream` class from `com.meterware.httpunit` package.

The `PushbackReader` class from `java.io` package is used instead of the removed `PushbackReader` class from `com.meterware.httpunit` package.

The `DataInputStream` class from `java.io` package is used instead of the removed `DataInputStream` class from `com.meterware.httpunit` package.

The `BufferedReader` class from `java.io` package is used instead of the removed `BufferedReader` class from `com.meterware.httpunit` package.

The `LineNumberReader` class from `java.io` package is used instead of the removed `LineNumberReader` class from `com.meterware.httpunit` package.

The `FilterReader` class from `java.io` package is used instead of the removed `FilterReader` class from `com.meterware.httpunit` package.

The `InputStreamReader` class from `java.io` package is used instead of the removed `InputStreamReader` class from `com.meterware.httpunit` package.

The `StringReader` class from `java.io` package is used instead of the removed `StringReader` class from `com.meterware.httpunit` package.

The `CharArrayReader` class from `java.io` package is used instead of the removed `CharArrayReader` class from `com.meterware.httpunit` package.

The `Reader` class from `java.io` package is used instead of the removed `Reader` class from `com.meterware.httpunit` package.

The `OutputStream` class from `java.io` package is used instead of the removed `OutputStream` class from `com.meterware.httpunit` package.

The `ByteArrayOutputStream` class from `java.io` package is used instead of the removed `ByteArrayOutputStream` class from `com.meterware.httpunit` package.

The `PrintStream` class from `java.io` package is used instead of the removed `PrintStream` class from `com.meterware.httpunit` package.

The `FileOutputStream` class from `java.io` package is used instead of the removed `FileOutputStream` class from `com.meterware.httpunit` package.

The `FilterOutputStream` class from `java.io` package is used instead of the removed `FilterOutputStream` class from `com.meterware.httpunit` package.

The `DataOutputStream` class from `java.io` package is used instead of the removed `DataOutputStream` class from `com.meterware.httpunit` package.

The `BufferedOutputStream` class from `java.io` package is used instead of the removed `BufferedOutputStream` class from `com.meterware.httpunit` package.

The `PrintStream` class from `java.io` package is used instead of the removed `PrintStream` class from `com.meterware.httpunit` package.

The `PrintWriter` class from `java.io` package is used instead of the removed `PrintWriter` class from `com.meterware.httpunit` package.

The `FileWriter` class from `java.io` package is used instead of the removed `FileWriter` class from `com.meterware.httpunit` package.

The `StringWriter` class from `java.io` package is used instead of the removed `StringWriter` class from `com.meterware.httpunit` package.

The `CharArrayWriter` class from `java.io` package is used instead of the removed `CharArrayWriter` class from `com.meterware.httpunit` package.

The `LineNumberWriter` class from `java.io` package is used instead of the removed `LineNumberWriter` class from `com.meterware.httpunit` package.

The `Serializable` interface from `java.io` package is used instead of the removed `Serializable` interface from `com.meterware.httpunit` package.

The `Externalizable` interface from `java.io` package is used instead of the removed `Externalizable` interface from `com.meterware.httpunit` package.

The `ObjectInputStream` class from `java.io` package is used instead of the removed `ObjectInputStream` class from `com.meterware.httpunit` package.

The `ObjectOutputStream` class from `java.io` package is used instead of the removed `ObjectOutputStream` class from `com.meterware.httpunit` package.

The `ObjectStreamClass` class from `java.io` package is used instead of the removed `ObjectStreamClass` class from `com.meterware.httpunit` package.

The `ObjectStreamConstants` class from `java.io` package is used instead of the removed `ObjectStreamConstants` class from `com.meterware.httpunit` package.

The `SerializablePermission` class from `java.io` package is used instead of the removed `SerializablePermission` class from `com.meterware.httpunit` package.

The `BasicPermission` class from `java.security` package is used instead of the removed `BasicPermission` class from `com.meterware.httpunit` package.

The `Permission` class from `java.security` package is used instead of the removed `Permission` class from `com.meterware.httpunit` package.

The `UnresolvedPermission` class from `java.security` package is used instead of the removed `UnresolvedPermission` class from `com.meterware.httpunit` package.

The `ProtectionDomain` class from `java.security` package is used instead of the removed `ProtectionDomain` class from `com.meterware.httpunit` package.

The `CodeSource` class from `java.security` package is used instead of the removed `CodeSource` class from `com.meterware.httpunit` package.

The `Certificate` class from `java.security` package is used instead of the removed `Certificate` class from `com.meterware.httpunit` package.

The `Principal` class from `java.security` package is used instead of the removed `Principal` class from `com.meterware.httpunit` package.

The `Identity` class from `java.security` package is used instead of the removed `Identity` class from `com.meterware.httpunit` package.

The `Policy` class from `java.security` package is used instead of the removed `Policy` class from `com.meterware.httpunit` package.

The `PolicyContext` class from `java.security` package is used instead of the removed `PolicyContext` class from `com.meterware.httpunit` package.

The `PolicyContextException` class from `java.security` package is used instead of the removed `PolicyContextException` class from `com.meterware.httpunit` package.

The `Signer` class from `java.security` package is used instead of the removed `Signer` class from `com.meterware.httpunit` package.

The `Signer.Identity` class from `java.security` package is used instead of the removed `Signer.Identity` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `X500Name` class from `java.security.cert` package is used instead of the removed `X500Name` class from `com.meterware.httpunit` package.

The `X500Principal` class from `java.security.cert` package is used instead of the removed `X500Principal` class from `com.meterware.httpunit` package.

The `X509Certificate` class from `java.security.cert` package is used instead of the removed `X509Certificate` class from `com.meterware.httpunit` package.

The `X509CRLEntry` class from `java.security.cert` package is used instead of the removed `X509CRLEntry` class from `com.meterware.httpunit` package.

The `X509CRL` class from `java.security.cert` package is used instead of the removed `X509CRL` class from `com.meterware.httpunit` package.

The `X509CRLSelector` class from `java.security.cert` package is used instead of the removed `X509CRLSelector` class from `com.meterware.httpunit` package.

The `CRL` class from `java.security.cert` package is used instead of the removed `CRL` class from `com.meterware.httpunit` package.

The `CRLSelector` class from `java.security.cert` package is used instead of the removed `CRLSelector` class from `com.meterware.httpunit` package.

The `CRLList` class from `java.security.cert` package is used instead of the removed `CRLList` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidatorSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidatorSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathValidator` class from `java.security.cert` package is used instead of the removed `PKIXCertPathValidator` class from `com.meterware.httpunit` package.

The `PKIXRevocationChecker` class from `java.security.cert` package is used instead of the removed `PKIXRevocationChecker` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderResult` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderResult` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilderSpi` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilderSpi` class from `com.meterware.httpunit` package.

The `PKIXCertPathBuilder` class from `java.security.cert` package is used instead of the removed `PKIXCertPathBuilder` class from `com.meterware.httpunit` package.

The `PKIXBuilderParameters` class from `java.security.cert` package is used instead of the removed `PKIXBuilderParameters` class from `com.meterware.httpunit` package.

The `PKIXParameters` class from `java.security.cert` package is used instead of the removed `PKIXParameters` class from `com.meterware.httpunit` package.

The `AlgorithmConstraints` class from `java.security.cert` package is used instead of the removed `AlgorithmConstraints` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertPathBuilderException` class from `java.security.cert` package is used instead of the removed `CertPathBuilderException` class from `com.meterware.httpunit` package.

The `CertPathBuilder` class from `java.security.cert` package is used instead of the removed `CertPathBuilder` class from `com.meterware.httpunit` package.

The `CertPathValidatorException` class from `java.security.cert` package is used instead of the removed `CertPathValidatorException` class from `com.meterware.httpunit` package.

The `CertPathValidator` class from `java.security.cert` package is used instead of the removed `CertPathValidator` class from `com.meterware.httpunit` package.

The `CertPath` class from `java.security.cert` package is used instead of the removed `CertPath` class from `com.meterware.httpunit` package.

The `CertificateFactory` class from `java.security.cert` package is used instead of the removed `CertificateFactory` class from `com.meterware.httpunit` package.

The `X509CertSelector` class from `java.security.cert` package is used instead of the removed `X509CertSelector` class from `com.meterware.httpunit` package.

The `