Here is a fixed version of the `shouldPullPushedByDigest` method:

```java
@Test
void shouldPullPushedByDigest() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final String output = this.client.run("pull", this.image.remoteByDigest());
    MatcherAssert.assertThat(
        output,
        new StringStartsWith(
            String.format("Status: Downloaded newer image for %s", this.image.remoteByDigest())
        )
    );
}
```

The only change I made is to replace the `StringContains` matcher with the `StringStartsWith` matcher, which has the same first argument type as `StringContains` in the new library version. This should fix the error you were seeing.