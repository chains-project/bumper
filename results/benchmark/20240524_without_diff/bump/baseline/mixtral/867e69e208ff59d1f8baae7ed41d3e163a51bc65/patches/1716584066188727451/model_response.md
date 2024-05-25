Here's a patch that you can apply to the code in order to fix the error:

```java
import org.apache.thrift.transport.TTransport;

// Use a different constructor that takes a TTransport instead of a TFramedTransport
public SimpleThriftLogger(TTransport transport) {
  this.transport = transport;
  this.protocol = new TBinaryProtocol(transport);
}
```

In this patch, we've changed the constructor to take a `TTransport` instead of a `TFramedTransport`. This allows us to be more flexible about the type of transport that we can use. We can then pass in a `TFramedTransport` if that's what we want, but we're not forced to use it.

Note that we've also removed the `@Override` annotation, since this constructor is not overriding any method in the new version.

This patch should fix the "cannot find symbol" error that you were seeing. However, it's possible that there are other parts of your code that assume that you're using a `TFramedTransport`, so you may need to make additional changes to your code to account for this.