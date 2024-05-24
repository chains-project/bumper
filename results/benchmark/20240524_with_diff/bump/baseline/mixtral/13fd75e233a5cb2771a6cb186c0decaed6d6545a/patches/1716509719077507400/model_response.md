Here is a fixed version of the `shouldPullPushedByDigest` method that should resolve the error:
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
The error was caused by the `StringContains` constructor being called with two arguments, while it only accepts one argument in the new library version. To fix the error, I removed the `false` argument from the `StringContains` constructor.