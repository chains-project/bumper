Here is a fixed version of the method using a different Hamcrest matcher, `StringMatchesPattern`:

```java
private static Matcher<String> imagePulled(final String image) {
    Pattern pattern = Pattern.compile(String.format("Downloaded newer image for %s", image));
    return new StringMatchesPattern(pattern);
}
```
This version uses a regular expression to match the output string, which should be more flexible than the original version.

Note that `StringMatchesPattern` is a new class added in Hamcrest 2.2, so it should be available in the version of Hamcrest that you are using.

Also, you may need to import the following class:
```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
```
And you can use the following code to test the method:
```java
@Test
public void testImagePulled() {
    String image = "test-image";
    String output = "Status: Downloaded newer image for " + image;
    assertThat(imagePulled(image).matches(output), is(true));
}
```
This test case will check if the output string matches the pattern, if it's true then the test case will pass.