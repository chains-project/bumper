Here's a possible patch for the code:

```java
    @Test
    void shouldPullPushedByDigest() throws Exception {
        this.client.run("push", this.image.remote());
        this.client.run("image", "rm", this.image.name());
        this.client.run("image", "rm", this.image.remote());
        final String output = this.client.run("pull", this.image.remoteByDigest());
        MatcherAssert.assertThat(
            output,
            new StringContains(String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest()))
        );
    }
```

The only change made is to remove the `false` argument from the `StringContains` constructor. According to the error message, this argument is no longer accepted by the constructor in the new version of the library.