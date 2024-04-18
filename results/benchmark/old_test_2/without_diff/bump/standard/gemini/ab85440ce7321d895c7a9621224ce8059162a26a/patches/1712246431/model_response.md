```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.StringContains.containsString;
...
    final java.lang.String digest = "123";
    blobs.put(new com.artipie.docker.asto.CheckedBlobSource(new com.artipie.asto.Content.From("data".getBytes()), new com.artipie.docker.Digest.Sha256(digest))).toCompletableFuture().handle(( blob, throwable) -> {
        assertThat("Exception thrown", throwable, new com.artipie.docker.asto.IsNot<>(new com.artipie.docker.asto.IsNull<>()));
        assertThat("Exception is InvalidDigestException", com.google.common.base.Throwables.getRootCause(throwable), new org.hamcrest.core.IsInstanceOf(com.artipie.docker.error.InvalidDigestException.class));
        assertThat("Exception message contains calculated digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), containsString("3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7"));
        assertThat("Exception message contains expected digest", com.google.common.base.Throwables.getRootCause(throwable).getMessage(), containsString(digest));
        return java.util.concurrent.CompletableFuture.allOf();
    }).join();
```