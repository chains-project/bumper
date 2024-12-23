```java
import org.cactoos.text.TrimmedText;

import java.util.Optional;

public class RtTransaction {

    public Optional<Long> getId() {
        return Optional.empty();
    }

    public void setAmount(String amount) {
        amount = new TrimmedText(amount).asString();

        if (amount.isEmpty()) {
            throw new IllegalArgumentException("Amount cannot be empty");
        }

        if (!amount.matches("[0-9]+")) {
            throw new IllegalArgumentException("Amount must be a positive integer");
        }

        this.amount = new BigDecimal(amount);
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public void setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
    }

    public void setCreatedBy(String createdBy) {
        this.createdBy = createdBy;
    }

    public void setUpdatedAt(String updatedAt) {
        this.updatedAt = updatedAt;
    }

    public void setUpdatedBy(String updatedBy) {
        this.updatedBy = updatedBy;
    }

    public void setDeletedAt(String deletedAt) {
        this.deletedAt = deletedAt;
    }

    public void setDeletedBy(String deletedBy) {
        this.deletedBy = deletedBy;
    }
}
```