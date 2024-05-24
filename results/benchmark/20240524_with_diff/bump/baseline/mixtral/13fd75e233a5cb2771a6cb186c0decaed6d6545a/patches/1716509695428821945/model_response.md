Here is a possible patch for the code you provided:

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

The only change I made is to replace the `StringContains` matcher with the `StringStartsWith` matcher. This is because the `StringContains` constructor that takes a `boolean` argument has been removed in the new library version, and the `StringStartsWith` matcher is a good alternative for checking if a string starts with a certain substring.

I also removed the `false` argument from the `StringStartsWith` constructor, because it is not necessary and it was causing a compilation error.

Note that this is just one possible solution, and there might be other ways to fix the code as well.