```java
import org.cactoos.text.UncheckedText;
import org.jetbrains.annotations.NotNull;

import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class RtTransaction {

    private final String hash;
    private final String blockHash;
    private final int blockNumber;
    private final int index;
    private final String from;
    private final String to;
    private final String value;
    private final String gasPrice;
    private final String gas;
    private final String input;
    private final String nonce;
    private final List<RtLog> logs;
    private final String confirmations;
    private final String status;

    public RtTransaction(String hash, String blockHash, int blockNumber, int index, String from, String to, String value, String gasPrice, String gas, String input, String nonce, List<RtLog> logs, String confirmations, String status) {
        this.hash = hash;
        this.blockHash = blockHash;
        this.blockNumber = blockNumber;
        this.index = index;
        this.from = from;
        this.to = to;
        this.value = value;
        this.gasPrice = gasPrice;
        this.gas = gas;
        this.input = input;
        this.nonce = nonce;
        this.logs = logs;
        this.confirmations = confirmations;
        this.status = status;
    }

    public String getHash() {
        return hash;
    }

    public String getBlockHash() {
        return blockHash;
    }

    public int getBlockNumber() {
        return blockNumber;
    }

    public int getIndex() {
        return index;
    }

    public String getFrom() {
        return from;
    }

    public String getTo() {
        return to;
    }

    public String getValue() {
        return value;
    }

    public String getGasPrice() {
        return gasPrice;
    }

    public String getGas() {
        return gas;
    }

    public String getInput() {
        return input;
    }

    public String getNonce() {
        return nonce;
    }

    public List<RtLog> getLogs() {
        return logs;
    }

    public String getConfirmations() {
        return confirmations;
    }

    public String getStatus() {
        return status;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        RtTransaction that = (RtTransaction) o;
        return blockNumber == that.blockNumber &&
                index == that.index &&
                Objects.equals(hash, that.hash) &&
                Objects.equals(blockHash, that.blockHash) &&
                Objects.equals(from, that.from) &&
                Objects.equals(to, that.to) &&
                Objects.equals(value, that.value) &&
                Objects.equals(gasPrice, that.gasPrice) &&
                Objects.equals(gas, that.gas) &&
                Objects.equals(input, that.input) &&
                Objects.equals(nonce, that.nonce) &&
                Objects.equals(logs, that.logs) &&
                Objects.equals(confirmations, that.confirmations) &&
                Objects.equals(status, that.status);
    }

    @Override
    public int hashCode() {
        return Objects.hash(hash, blockHash, blockNumber, index, from, to, value, gasPrice, gas, input, nonce, logs, confirmations, status);
    }

    @Override
    public String toString() {
        return new UncheckedText(
                "RtTransaction{" +
                        "hash='" + hash + '\'' +
                        ", blockHash='" + blockHash + '\'' +
                        ", blockNumber=" + blockNumber +
                        ", index=" + index +
                        ", from='" + from + '\'' +
                        ", to='" + to + '\'' +
                        ", value='" + value + '\'' +
                        ", gasPrice='" + gasPrice + '\'' +
                        ", gas='" + gas + '\'' +
                        ", input='" + input + '\'' +
                        ", nonce='" + nonce + '\'' +
                        ", logs=" + logs +
                        ", confirmations='" + confirmations + '\'' +
                        ", status='" + status + '\'' +
                        '}'
        ).asString();
    }

    public static class Builder {
        private String hash;
        private String blockHash;
        private int blockNumber;
        private int index;
        private String from;
        private String to;
        private String value;
        private String gasPrice;
        private String gas;
        private String input;
        private String nonce;
        private List<RtLog> logs;
        private String confirmations;
        private String status;

        public Builder setHash(String hash) {
            this.hash = hash;
            return this;
        }

        public Builder setBlockHash(String blockHash) {
            this.blockHash = blockHash;
            return this;
        }

        public Builder setBlockNumber(int blockNumber) {
            this.blockNumber = blockNumber;
            return this;
        }

        public Builder setIndex(int index) {
            this.index = index;
            return this;
        }

        public Builder setFrom(String from) {
            this.from = from;
            return this;
        }

        public Builder setTo(String to) {
            this.to = to;
            return this;
        }

        public Builder setValue(String value) {
            this.value = value;
            return this;
        }

        public Builder setGasPrice(String gasPrice) {
            this.gasPrice = gasPrice;
            return this;
        }

        public Builder setGas(String gas) {
            this.gas = gas;
            return this;
        }

        public Builder setInput(String input) {
            this.input = input;
            return this;
        }

        public Builder setNonce(String nonce) {
            this.nonce = nonce;
            return this;
        }

        public Builder setLogs(List<RtLog> logs) {
            this.logs = logs;
            return this;
        }

        public Builder setConfirmations(String confirmations) {
            this.confirmations = confirmations;
            return this;
        }

        public Builder setStatus(String status) {
            this.status = status;
            return this;
        }

        public RtTransaction build() {
            return new RtTransaction(hash, blockHash, blockNumber, index, from, to, value, gasPrice, gas, input, nonce, logs, confirmations, status);
        }
    }

    public static class RtLog {
        private final String logIndex;
        private final String transactionIndex;
        private final String transactionHash;
        private final String blockHash;
        private final String blockNumber;
        private final String address;
        private final String data;
        private final List<String> topics;

        public RtLog(String logIndex, String transactionIndex, String transactionHash, String blockHash, String blockNumber, String address, String data, List<String> topics) {
            this.logIndex = logIndex;
            this.transactionIndex = transactionIndex;
            this.transactionHash = transactionHash;
            this.blockHash = blockHash;
            this.blockNumber = blockNumber;
            this.address = address;
            this.data = data;
            this.topics = topics;
        }

        public String getLogIndex() {
            return logIndex;
        }

        public String getTransactionIndex() {
            return transactionIndex;
        }

        public String getTransactionHash() {
            return transactionHash;
        }

        public String getBlockHash() {
            return blockHash;
        }

        public String getBlockNumber() {
            return blockNumber;
        }

        public String getAddress() {
            return address;
        }

        public String getData() {
            return data;
        }

        public List<String> getTopics() {
            return topics;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            RtLog rtLog = (RtLog) o;
            return Objects.equals(logIndex, rtLog.logIndex) &&
                    Objects.equals(transactionIndex, rtLog.transactionIndex) &&
                    Objects.equals(transactionHash, rtLog.transactionHash) &&
                    Objects.equals(blockHash, rtLog.blockHash) &&
                    Objects.equals(blockNumber, rtLog.blockNumber) &&
                    Objects.equals(address, rtLog.address) &&
                    Objects.equals(data, rtLog.data) &&
                    Objects.equals(topics, rtLog.topics);
        }

        @Override
        public int hashCode() {
            return Objects.hash(logIndex, transactionIndex, transactionHash, blockHash, blockNumber, address, data, topics);
        }

        @Override
        public String toString() {
            return new UncheckedText(
                    "RtLog{" +
                            "logIndex='" + logIndex + '\'' +
                            ", transactionIndex='" + transactionIndex + '\'' +
                            ", transactionHash='" + transactionHash + '\'' +
                            ", blockHash='" + blockHash + '\'' +
                            ", blockNumber='" + blockNumber + '\'' +
                            ", address='" + address + '\'' +
                            ", data='" + data + '\'' +
                            ", topics=" + topics +
                            '}'
            ).asString();
        }

        public static class Builder {
            private String logIndex;
            private String transactionIndex;
            private String transactionHash;
            private String blockHash;
            private String blockNumber;
            private String address;
            private String data;
            private List<String> topics;

            public Builder setLogIndex(String logIndex) {
                this.logIndex = logIndex;
                return this;
            }

            public Builder setTransactionIndex(String transactionIndex) {
                this.transactionIndex = transactionIndex;
                return this;
            }

            public Builder setTransactionHash(String transactionHash) {
                this.transactionHash = transactionHash;
                return this;
            }

            public Builder setBlockHash(String blockHash) {
                this.blockHash = blockHash;
                return this;
            }

            public Builder setBlockNumber(String blockNumber) {
                this.blockNumber = blockNumber;
                return this;
            }

            public Builder setAddress(String address) {
                this.address = address;
                return this;
            }

            public Builder setData(String data) {
                this.data = data;
                return this;
            }

            public Builder setTopics(List<String> topics) {
                this.topics = topics;
                return this;
            }

            public RtLog build() {
                return new RtLog(logIndex, transactionIndex, transactionHash, blockHash, blockNumber, address, data, topics);
            }
        }
    }
}
```