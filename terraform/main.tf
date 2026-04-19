provider "aws" {
  region = "us-east-1"
}

# [FINANCE] Aladdin Infrastructure Simulation
# Auto-Scaling Group for financial microservices
resource "aws_launch_template" "aladdin_svc" {
  name_prefix   = "aladdin-service-"
  image_id      = "ami-0c101f26f147fa7fd"
  instance_type = "t3.medium"
}

resource "aws_autoscaling_group" "aladdin_asg" {
  name                = "aladdin-core-asg"
  vpc_zone_identifier = ["subnet-12345678"] # Dummy subnet
  desired_capacity    = 2
  max_size            = 10
  min_size            = 2

  launch_template {
    id      = aws_launch_template.aladdin_svc.id
    version = "$Latest"
  }

  tag {
    key                 = "Project"
    value               = "Aladdin-Reliability-Guard"
    propagate_at_launch = true
  }
}

# [METRICS] FinOps Guard: CloudWatch Metric for Cost/Usage Tracking
resource "aws_cloudwatch_metric_alarm" "high_cost_usage" {
  alarm_name          = "aladdin-high-compute-usage"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "300"
  statistic           = "Average"
  threshold           = "80"
  alarm_description   = "Monitoring for efficiency. High usage outside market hours requires AI-remediation."
  alarm_actions       = [aws_sns_topic.alerts.arn]
}

resource "aws_sns_topic" "alerts" {
  name = "aladdin-guard-alerts"
}

# [SECURITY] Security & Compliance: S3 for Aladdin Data with Encryption
resource "aws_s3_bucket" "financial_data" {
  bucket = "blackrock-aladdin-data-demo"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data_encryption" {
  bucket = aws_s3_bucket.financial_data.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
