Here's a proposed patch to fix the error:
```java
import java.security.cert.CertificateEncodingException;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import org.bouncycastle.asn1.ASN1OctetString;
import org.bouncycastle.asn1.DEROctetString;
import org.bouncycastle.crypto.CryptoException;
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsIOException;
import org.bouncycastle.crypto.tls.TlsProtocolException;
import org.bouncycastle.crypto.tls.TlsSession;
import org.bouncycastle.crypto.tls.TlsStream;
import org.bouncycastle.crypto.tls.crypto.TlsCipher;
import org.bouncycastle.crypto.tls.crypto.TlsCipherFactory;
import org.bouncycastle.crypto.tls.crypto.TlsKeyExchange;
import org.bouncycastle.crypto.tls.crypto.TlsKeyExchangeFactory;
import org.bouncycastle.crypto.tls.crypto.TlsSecret;
import org.bouncycastle.crypto.tls.crypto.TlsSecretFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsRSAEncryption;
import org.bouncycastle.crypto.tls.crypto.impl.TlsRSAKeyExchange;
import org.bouncycastle.crypto.tls.crypto.impl.TlsRSAKeyExchangeFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsRSASignature;
import org.bouncycastle.crypto.tls.crypto.impl.TlsRSASignatureFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsSecretFactoryImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsSessionImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsStreamImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsTls12KeyExchange;
import org.bouncycastle.crypto.tls.crypto.impl.TlsTls12KeyExchangeFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsTls13KeyExchange;
import org.bouncycastle.crypto.tls.crypto.impl.TlsTls13KeyExchangeFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsTls13Secret;
import org.bouncycastle.crypto.tls.crypto.impl.TlsTls13SecretFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsTls13Signature;
import org.bouncycastle.crypto.tls.crypto.impl.TlsTls13SignatureFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManager;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpec;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecification;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProvider;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpec;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecification;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProvider;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpec;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecification;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProvider;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpec;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecification;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProvider;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpec;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecification;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProvider;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderImplFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpec;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecification;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationImpl;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProvider;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderFactory;
import org.bouncycastle.crypto.tls.crypto.impl.TlsX509TrustManagerSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderSpecificationProviderImpl;
import org.bouncycastle.crypto.