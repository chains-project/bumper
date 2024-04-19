Here is a possible patch for the failing method:
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
The failure is caused by the fact that the constructor of `StringContains` now requires a single `String` argument, instead of a `boolean` and a `String`. To fix the failure, I replaced the `StringContains` matcher with a `StringStartsWith` matcher, which checks if a string starts with a given substring. This matcher only has a single constructor that takes a `String` argument, so it is compatible with the new library version.