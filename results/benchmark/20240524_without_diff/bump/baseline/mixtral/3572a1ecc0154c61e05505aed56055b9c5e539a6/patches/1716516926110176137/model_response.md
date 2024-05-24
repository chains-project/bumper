Here's a possible patch for the failing code:

```java
import org.apache.thrift.transport.TIOStreamTransport;

import java.io.InputStream;
import java.io.OutputStream;

public class AppenderUtils {
    // ...

    private static TTransport createFramedTransport(TTransport transport) {
        return new TFramedTransport(transport);
    }

    private static TTransport createFastFramedTransport(TTransport transport, int frameSize, int bufferSize) {
        return new TFastFramedTransport(transport, frameSize, bufferSize);
    }

    private static TTransport createTIOStreamTransport(TConfiguration conf, InputStream in, OutputStream out) {
        return new TIOStreamTransport(conf, in, out);
    }

    // ...
}
```

This patch introduces three new methods:

1. `createFramedTransport`: creates a `TFramedTransport` instance using the given `TTransport` instance.
2. `createFastFramedTransport`: creates a `TFastFramedTransport` instance using the given `TTransport`, frame size, and buffer size.
3. `createTIOStreamTransport`: creates a `TIOStreamTransport` instance using the given `TConfiguration`, input stream, and output stream.

These methods replace the usage of deprecated constructors with new methods that achieve the same functionality.

Note that `TFramedTransport$Factory` and `TFastFramedTransport$Factory` classes have been removed in the new library version, so we can't use them anymore. Instead, we use the constructors directly.

Additionally, the `TIOStreamTransport` constructor has been changed in the new library version, so we need to use the new constructor that accepts a `TConfiguration` object. If you don't have a `TConfiguration` object, you can create a default one using `new TConfiguration()`.

I hope this helps! Let me know if you have any questions.