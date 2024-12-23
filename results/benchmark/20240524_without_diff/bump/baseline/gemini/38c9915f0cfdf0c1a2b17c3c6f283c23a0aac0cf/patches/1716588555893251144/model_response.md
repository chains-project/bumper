```java
import org.cactoos.scalar.UncheckedScalar;
import org.cactoos.scalar.Unchecked;

import java.util.Optional;

public class RtTransaction implements RtTransactionInterface {

    private final RtTransactionInterface transaction;

    public RtTransaction(RtTransactionInterface transaction) {
        this.transaction = transaction;
    }

    @Override
    public Optional<String> getRtTransactionId() {
        return transaction.getRtTransactionId();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionIdOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionId().orElseThrow(() -> new RuntimeException("RtTransactionId is not present")));
    }

    @Override
    public Optional<String> getRtTransactionType() {
        return transaction.getRtTransactionType();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionTypeOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionType().orElseThrow(() -> new RuntimeException("RtTransactionType is not present")));
    }

    @Override
    public Optional<String> getRtTransactionStatus() {
        return transaction.getRtTransactionStatus();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionStatusOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionStatus().orElseThrow(() -> new RuntimeException("RtTransactionStatus is not present")));
    }

    @Override
    public Optional<String> getRtTransactionTimestamp() {
        return transaction.getRtTransactionTimestamp();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionTimestampOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionTimestamp().orElseThrow(() -> new RuntimeException("RtTransactionTimestamp is not present")));
    }

    @Override
    public Optional<String> getRtTransactionAmount() {
        return transaction.getRtTransactionAmount();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionAmountOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionAmount().orElseThrow(() -> new RuntimeException("RtTransactionAmount is not present")));
    }

    @Override
    public Optional<String> getRtTransactionCurrency() {
        return transaction.getRtTransactionCurrency();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionCurrencyOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionCurrency().orElseThrow(() -> new RuntimeException("RtTransactionCurrency is not present")));
    }

    @Override
    public Optional<String> getRtTransactionFee() {
        return transaction.getRtTransactionFee();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionFeeOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionFee().orElseThrow(() -> new RuntimeException("RtTransactionFee is not present")));
    }

    @Override
    public Optional<String> getRtTransactionFeeCurrency() {
        return transaction.getRtTransactionFeeCurrency();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionFeeCurrencyOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionFeeCurrency().orElseThrow(() -> new RuntimeException("RtTransactionFeeCurrency is not present")));
    }

    @Override
    public Optional<String> getRtTransactionSender() {
        return transaction.getRtTransactionSender();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionSenderOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionSender().orElseThrow(() -> new RuntimeException("RtTransactionSender is not present")));
    }

    @Override
    public Optional<String> getRtTransactionReceiver() {
        return transaction.getRtTransactionReceiver();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionReceiverOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionReceiver().orElseThrow(() -> new RuntimeException("RtTransactionReceiver is not present")));
    }

    @Override
    public Optional<String> getRtTransactionNetwork() {
        return transaction.getRtTransactionNetwork();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionNetworkOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionNetwork().orElseThrow(() -> new RuntimeException("RtTransactionNetwork is not present")));
    }

    @Override
    public Optional<String> getRtTransactionHash() {
        return transaction.getRtTransactionHash();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionHashOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionHash().orElseThrow(() -> new RuntimeException("RtTransactionHash is not present")));
    }

    @Override
    public Optional<String> getRtTransactionBlockHeight() {
        return transaction.getRtTransactionBlockHeight();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionBlockHeightOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionBlockHeight().orElseThrow(() -> new RuntimeException("RtTransactionBlockHeight is not present")));
    }

    @Override
    public Optional<String> getRtTransactionBlockTimestamp() {
        return transaction.getRtTransactionBlockTimestamp();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionBlockTimestampOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionBlockTimestamp().orElseThrow(() -> new RuntimeException("RtTransactionBlockTimestamp is not present")));
    }

    @Override
    public Optional<String> getRtTransactionConfirmationCount() {
        return transaction.getRtTransactionConfirmationCount();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionConfirmationCountOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionConfirmationCount().orElseThrow(() -> new RuntimeException("RtTransactionConfirmationCount is not present")));
    }

    @Override
    public Optional<String> getRtTransactionMemo() {
        return transaction.getRtTransactionMemo();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionMemoOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionMemo().orElseThrow(() -> new RuntimeException("RtTransactionMemo is not present")));
    }

    @Override
    public Optional<String> getRtTransactionExtra() {
        return transaction.getRtTransactionExtra();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionExtraOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionExtra().orElseThrow(() -> new RuntimeException("RtTransactionExtra is not present")));
    }

    @Override
    public Optional<String> getRtTransactionError() {
        return transaction.getRtTransactionError();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionErrorOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionError().orElseThrow(() -> new RuntimeException("RtTransactionError is not present")));
    }

    @Override
    public Optional<String> getRtTransactionErrorCode() {
        return transaction.getRtTransactionErrorCode();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionErrorCodeOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionErrorCode().orElseThrow(() -> new RuntimeException("RtTransactionErrorCode is not present")));
    }

    @Override
    public Optional<String> getRtTransactionErrorMessage() {
        return transaction.getRtTransactionErrorMessage();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionErrorMessageOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionErrorMessage().orElseThrow(() -> new RuntimeException("RtTransactionErrorMessage is not present")));
    }

    @Override
    public Optional<String> getRtTransactionErrorStacktrace() {
        return transaction.getRtTransactionErrorStacktrace();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionErrorStacktraceOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionErrorStacktrace().orElseThrow(() -> new RuntimeException("RtTransactionErrorStacktrace is not present")));
    }

    @Override
    public Optional<String> getRtTransactionErrorData() {
        return transaction.getRtTransactionErrorData();
    }

    @Override
    public UncheckedScalar<String> getRtTransactionErrorDataOrThrow() {
        return new UncheckedScalar<>(transaction.getRtTransactionErrorData().orElseThrow(() -> new RuntimeException("RtTransactionErrorData is not present")));
    }
}
```