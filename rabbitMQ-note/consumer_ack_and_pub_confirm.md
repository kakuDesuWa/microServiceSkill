# Summaried From https://www.rabbitmq.com/confirms.html

Acknowledgements: Delivery processing acknowledgements from consumers to RabbitMQ are known as acknowledgements in AMQP 0-9-1 parlance.

Publish Confirms: Broker acknowledgements to publisher are a protocol extension called publisher confirm.

- Delivery Tags

Before we proceed to discuss other topics it is important to explain how deliveries are identified (and acknowledgements indicate their respective deliveries). When a consumer (subscription) is registered, messages will be delivered (pushed) by RabbitMQ using the basic.deliver method. The method carries a delivery tag, which uniquely identifies the delivery on a channel. Delivery tags are therefore scoped per channel.

Delivery tags are monotonically growing positive integers and are presented as such by client libraries. Client library methods that acknowledge deliveries take a delivery tag as an argument.

Because delivery tags are scoped per channel, deliveries must be acknowledged on the same channel they were received on. Acknowledging on a different channel will result in an "unknown delivery tag" protocol exception and close the channel.

- Consumer Acknowledgement Modes and Data Safety Considerations

When a node delivers a message to a consumer, it has to decide whether the message should be considered handled (or at least received) by the consumer. Since multiple things (client connections, consumer apps, and so on) can fail, this decision is a data safety concern. Messaging protocols usually provide a confirmation mechanism that allows consumers to acknowledge deliveries to the node they are connected to. Whether the mechanism is used is decided at the time consumer subscribes.

Depending on the acknowledgement mode used, RabbitMQ can consider a message to be successfully delivered either immediately after it is sent out (written to a TCP socket) or when an explicit ("manual") client acknowledgement is received. Manually sent acknowledgements can be positive or negative and use one of the following protocol methods:

basic.ack is used for positive acknowledgements

basic.nack is used for negative acknowledgements (note: this is a RabbitMQ extension to AMQP 0-9-1)

basic.reject is used for negative acknowledgements but has one limitation compared to basic.nack

In automatic acknowledgement mode, a message is considered to be successfully delivered immediately after it is sent. This mode trades off higher throughput (as long as the consumers can keep up) for reduced safety of delivery and consumer processing. This mode is often referred to as "fire-and-forget". Unlike with manual acknowledgement model, if consumers's TCP connection or channel is closed before successful delivery, the message sent by the server will be lost. Therefore, automatic message acknowledgement should be considered unsafe and not suitable for all workloads.

Acknowledging Multiple Deliveries at Once
