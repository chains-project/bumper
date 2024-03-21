Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        coverage.getClassInfo(Collections.singleton(data.getMutatedClass()), new org.pitest.classinfo.ClassInfoBuilder() {
            public org.pitest.classinfo.ClassInfo getClassInfo(org.pitest.classinfo.ClassName name, byte[] bytes, long time) {
                return new org.pitest.classinfo.ClassInfo(name, bytes, time);
            }
        }).getClassInfo(data.getMutatedClass()));
    }
```
The `getClassInfo` method has been removed from the `CoverageDatabase` class, so we need to use the `ClassInfoBuilder` class to create a new `ClassInfo` instance. We create a new `ClassInfoBuilder` instance and override its `getClassInfo` method to return a new `ClassInfo` instance with the given name, bytes, and time. We then pass this `ClassInfoBuilder` instance to the `getClassInfo` method of the `CoverageDatabase` class, which will call the overridden `getClassInfo` method of the `ClassInfoBuilder` instance and return the created `ClassInfo` instance.


This patch should fix the error and allow the code to compile and run correctly.