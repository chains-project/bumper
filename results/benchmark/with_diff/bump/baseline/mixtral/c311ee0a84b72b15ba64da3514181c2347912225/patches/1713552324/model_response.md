Here's a possible patch for the failing code:

```java
@Test
void shouldPullPushedByTag() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    String output = this.client.run("pull", this.image.remote());
    MatcherAssert.assertThat(
        output,
        new StringContains(String.format("Status: Downloaded newer image for %s", this.image.remote()))
    );
}
```

The change I made is to remove the `false` argument from the `StringContains` constructor. According to the error message, the constructor now only takes a single `String` argument, whereas before it took a `String` and a `boolean`. Since the `boolean` argument is not being used in this case, it can simply be removed.