Here's the fixed version of the `shouldPullPushedByTag` method:

```java
@Test
void shouldPullPushedByTag() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    final String output = this.client.run("pull", this.image.remote());
    MatcherAssert.assertThat(
        output,
        new StringStartsWith(
            String.format("Status: Downloaded newer image for %s", this.image.remote())
        )
    );
}
```

The fix involves changing the `StringContains` matcher to `StringStartsWith` to match the new library version. This is because the constructor of `StringContains` now requires a single argument, while the old version accepted two arguments.