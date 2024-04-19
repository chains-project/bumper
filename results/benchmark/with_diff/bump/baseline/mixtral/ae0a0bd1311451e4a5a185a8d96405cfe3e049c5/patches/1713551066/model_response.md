Here is a possible patch for the failing code:
```java
@Test
void shouldPullPushedByTag() throws Exception {
    this.client.run("push", this.image.remote());
    this.client.run("image", "rm", this.image.name());
    this.client.run("image", "rm", this.image.remote());
    String output = this.client.run("pull", this.image.remote());
    MatcherAssert.assertThat(
        output,
        new StringContains("Status: Downloaded newer image for " + this.image.remote())
    );
}
```
The change I made is to remove the `false` argument from the `StringContains` constructor. This is because the `StringContains` constructor with two arguments was removed in the new library version, and replaced with a constructor that takes only one argument. The `StringContains` matcher matches a string if it contains the specified substring, so there is no need to pass a boolean flag indicating whether the match should be exact or not.