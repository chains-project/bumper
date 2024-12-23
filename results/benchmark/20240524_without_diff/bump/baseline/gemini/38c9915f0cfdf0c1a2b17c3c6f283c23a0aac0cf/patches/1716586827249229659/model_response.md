```java
import org.cactoos.scalar.UncheckedScalar;
import org.cactoos.scalar.Unchecked;

import java.util.function.Function;

public interface RtTransaction extends AutoCloseable {

    /**
     * The transaction will be rolled back if an error occurs.
     *
     * @param function the function to execute
     * @param <T>      the return type of the function
     * @return the result of the function
     */
    <T> T execute(Function<RtTransaction, T> function);

    /**
     * The transaction will be rolled back if an error occurs.
     *
     * @param function the function to execute
     * @return the result of the function
     */
    default void execute(Unchecked function) {
        execute(transaction -> {
            function.apply();
            return null;
        });
    }

    /**
     * The transaction will be rolled back if an error occurs.
     *
     * @param function the function to execute
     * @param <T>      the return type of the function
     * @return the result of the function
     */
    <T> T executeUnchecked(Function<RtTransaction, T> function) {
        return new UncheckedScalar<>(execute(function)).value();
    }

    /**
     * The transaction will be rolled back if an error occurs.
     *
     * @param function the function to execute
     * @return the result of the function
     */
    default void executeUnchecked(Unchecked function) {
        executeUnchecked(transaction -> {
            function.apply();
            return null;
        });
    }
}
```