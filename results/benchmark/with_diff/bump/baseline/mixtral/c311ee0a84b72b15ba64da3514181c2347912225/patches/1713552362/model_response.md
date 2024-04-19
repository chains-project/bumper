Here is a proposed patch for the failing method:
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
The only change made is the removal of the `false` argument from the `StringContains` constructor. This is because the constructor for `StringContains` no longer accepts a `boolean` argument in the new library version. Instead, it only accepts a single `String` argument. The `String.format` method is used to construct the expected string to be matched.