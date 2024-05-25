Here's a proposed patch for the failing client code:

```java
@Test
void failsOnDigestMismatch() {
    final InMemoryStorage storage = new InMemoryStorage();
    final AstoBlobs blobs = new AstoBlobs(
            storage, new DefaultLayout(), new RepoName.Simple("any")
    );
    final String digest = "123";
    final Content content = new Content.From("data".getBytes());
    final Digest calculatedDigest = new Digest.Sha256(content.checksum());
    blobs.put(
            new CheckedBlobSource(content, calculatedDigest)
    ).toCompletableFuture().handle(
            (blob, throwable) -> {
                assertThat(throwable, notNullValue());
                assertThat(throwable, instanceOf(InvalidDigestException.class));
                assertThat(throwable.getMessage(), stringContainsInOrder(
                        calculatedDigest.asHex(),
                        digest
                ));
                return CompletableFuture.allOf();
            }
    ).join();
}
```

In this patch, I created new variables `content` and `calculatedDigest` for better readability. I also replaced the `JUnit413StringContains` matcher with `stringContainsInOrder` from the Hamcrest library. This method checks if a string contains a sequence of substrings, so it can be used to check if the exception message contains both the calculated digest and the expected digest.

Note that the `JUnit413StringContains` matcher may not be available in newer versions of JUnit, so I used a different matcher that achieves the same goal. Also, the `notNullValue` and `instanceOf` matchers are from the Hamcrest library as well.

Finally, I removed the `Override` decorator from the method signature because it is not overriding any method in the new version.