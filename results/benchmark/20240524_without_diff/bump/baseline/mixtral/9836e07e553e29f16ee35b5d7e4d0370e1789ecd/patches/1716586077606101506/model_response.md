Here's the proposed patch to fix the error:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.hasItem;
import static org.hamcrest.Matchers.stringContainsInOrder;

import java.util.Arrays;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

class TagValidTest {

    @ParameterizedTest
    @ValueSource(strings = {
        "",
        ".0",
        "*",
        "\u00ea",
        "-my-tag",
        "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678"
    })
    void shouldFailToGetValueWhenInvalid(final String original) {
        final Tag.Valid tag = new Tag.Valid(original);
        assertThat(tag.valid(), new IsEqual<>(false));
        final InvalidTagNameException exception = Assertions.assertThrows(
            InvalidTagNameException.class,
            tag::value
        );
        assertThat(
            exception.getMessage(),
            allOf(
                hasItem(stringContainsInOrder(Arrays.asList("Invalid tag", original)))
            )
        );
    }
}
```

In this patch, I replaced `StringContains` with `stringContainsInOrder` from the `Matchers` class, which is an added library method identified with `++`. This method checks if the given string contains the substrings in the order they appear in the list.